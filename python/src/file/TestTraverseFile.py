# -*- coding: utf-8 -*-

# __author__ = xiaobao
# __date__ = 2018/12/21 15:03:01

# desc: 遍历文件夹

import os


def TraverseDir(szCurDir, szSubDir):
    # 遍历filepath下所有文件，包括子目录
    listDir = os.listdir(szCurDir)
    for szDir in listDir:
        szFullDir = os.path.join(szCurDir, szDir)
        if os.path.isdir(szFullDir):
            TraverseDir(szFullDir, os.path.join(szSubDir, szDir))
        else:
            if szSubDir == "":
                print szDir
            else:
                print szSubDir + "/" + szDir


TraverseDir("F:/dest", "")
