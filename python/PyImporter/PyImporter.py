# -*- coding: utf-8 -*-

# 需要先检查是否加载__init__.py文件
# 然后加载文件

# import C_file

import os
import imp

class C_file(object):
    ext = "py"
    def __init__(self):
        pass

    @classmethod
    def find_file(cls, szPkgName, szPath):
        szFullPath = szPath + "/py/" + szPkgName

        print("C_file.find_file", szPkgName, szPath, szFullPath)
        if(os.path.exists(szFullPath)):
            return True

        return False

    @classmethod
    def get_file(cls, szName, szPath):
        szFullPath = szPath + "/py/" + szName
        print("C_file.get_file", szName, szPath, szFullPath)

        with open(szFullPath, "r") as f:
            # szLines = f.readlines() 
            szText = f.read()
            print("xjcprint---------------PyImporter", szText)
            return szText
            # return szLines

        return ""

    @classmethod
    def new_module(cls, szName, szData, szPath):
        print("C_file.new_module", szName, szData, szPath)

        return ""


class PyImporter(object):
    ext = '.py'

    def __init__(self, path):
        print("xjc__init__", path)
        self._path = path

    def _get__path__(self):
        return [self._path]

    def find_module(self, fullname, path=None):
        print("xjc__find_module", fullname, path)
        oldfullname = fullname

        if path is None:
            path = self._path

        fullname = fullname.replace('.', '/')
        pkg_name = fullname + "/__init__" + PyImporter.ext

        if C_file.find_file(pkg_name, path):
            return self

        fullname += PyImporter.ext

        if C_file.find_file(fullname, path):
            return self
        else:
            return None

    def load_module(self, fullname):
        print("xjc__load_module", fullname)
        is_pkg = True
        mod_path = fullname.replace('.', '/') + "/__init__"
        mod_name = fullname
        if not C_file.find_file(mod_path + PyImporter.ext, self._path):
            is_pkg = False
            mod_path = fullname.replace('.', '/')
            mod_name = fullname

        data = C_file.get_file(mod_path + PyImporter.ext, self._path)
        data = data.replace("\r\n", "\n")

        mod = sys.modules.setdefault(fullname, imp.new_module(fullname))
        mod.__file__ = "<%s>" % self.__class__.__name__
        mod.__loader__ = self
        if is_pkg:
            mod.__path__ = self._get__path__()

        exec data in mod.__dict__
        return mod


class Watcher(object):
    @classmethod
    def find_module(cls, name, path, target=None):
        print("Importing", name, path, target)
        return None

try:
    import sys

    # ********************************************************************************
    # pyimporter代码
    # ********************************************************************************
    print(sys.path_hooks)
    # sys.path_hooks[len(sys.path_hooks)-1] = PyImporter
    sys.path_hooks.append(PyImporter)
    # sys.path.append("!!!!!test path!!!!!!!!!!")
    sys.path_importer_cache.clear()


    # ********************************************************************************
    # create module from code
    # ********************************************************************************
    # import sys,imp
    # my_code = "a = 5"
    # mymodule = imp.new_module("mymodule")
    # exec my_code in mymodule.__dict__
    # sys.modules["mymodule"] = mymodule

    # import mymodule
    # print(mymodule.a)

    # ********************************************************************************
    # 重载c_file，实现重定向py文件
    # ********************************************************************************
    # import Zz
    # import py.pymain
    # import py.pymain.maintest

    try:
        import pymain
        import pymain.maintest
        print(sys.path_importer_cache)
    except Exception, e:
        print(e)

        # print(sys.path)
        # print(sys.modules)
        print(sys.path_importer_cache)



except Exception, e:
    print(e)
    pass
