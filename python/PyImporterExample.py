import sys

from importlib.abc import FileLoader
from importlib.machinery import FileFinder, PathFinder
from os import getcwd
from os.path import basename

from sibilant.module import prep_module, exec_module


SOURCE_SUFFIXES = [".lspy", ".sibilant"]


_path_importer_cache = {}
_path_hooks = []


class SibilantPathFinder(PathFinder):
    """
    An overridden PathFinder which will hunt for sibilant files in
    sys.path. Uses storage in this module to avoid conflicts with the
    original PathFinder
    """


    @classmethod
    def invalidate_caches(cls):
        for finder in _path_importer_cache.values():
            if hasattr(finder, 'invalidate_caches'):
                finder.invalidate_caches()


    @classmethod
    def _path_hooks(cls, path):
        for hook in _path_hooks:
            try:
                return hook(path)
            except ImportError:
                continue
        else:
            return None


    @classmethod
    def _path_importer_cache(cls, path):
        if path == '':
            try:
                path = getcwd()
            except FileNotFoundError:
                # Don't cache the failure as the cwd can easily change to
                # a valid directory later on.
                return None
        try:
            finder = _path_importer_cache[path]
        except KeyError:
            finder = cls._path_hooks(path)
            _path_importer_cache[path] = finder
        return finder


class SibilantSourceFileLoader(FileLoader):


    def create_module(self, spec):
        return None


    def get_source(self, fullname):
        return self.get_data(self.get_filename(fullname)).decode("utf8")


    def exec_module(self, module):
        name = module.__name__
        source = self.get_source(name)
        filename = basename(self.get_filename(name))

        prep_module(module)
        exec_module(module, source, filename=filename)


def _get_lspy_file_loader():
    return (SibilantSourceFileLoader, SOURCE_SUFFIXES)


def _get_lspy_path_hook():
    return FileFinder.path_hook(_get_lspy_file_loader())


def _install():
    done = False

    def install():
        nonlocal done
        if not done:
            _path_hooks.append(_get_lspy_path_hook())
            sys.meta_path.append(SibilantPathFinder)
            done = True

    return install


_install = _install()
_install()