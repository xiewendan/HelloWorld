# -*- coding: utf-8 -*-

# __author__ = xiaobao
# __date__ = 2018/12/21 15:38:37

# desc: 移除文件和文件夹

import os

import shutil

def RemoveFile(szFile):
    if not os.path.exists(szFile):
        return
    if os.path.exists(szFile) and os.path.isfile(szFile):
        os.remove(szFile)
    else:
        shutil.rmtree(szFile)

RemoveFile("F:/dest")

# System.IO.File.WriteAllBytes("F:/dest/1.txt", "xjc");