using System;
using System.IO;
using System.Text.RegularExpressions;

public class ParseNewestPath
{
    // 从路径中解析出时间，输入为：patch1529441477.yt.all.ios.zip
    static public Int64 GetTime(string szPath)
    {
        string szPattern = @"\d*";

        foreach (Match match in Regex.Matches(szPath, szPattern))
        {
            if (match.Value.Length > 0)
            {
                return Int64.Parse(match.Value);
            }
        }
        return Int64.MinValue;
    }
    // 遍历得到某个目录下面，命名中包含时间，时间最近的zip的路径打印出来
    static public void GetPrintNewestPath()
    {
        DirectoryInfo dir = new DirectoryInfo(@"E:\project\dm109\tools\GameEngine\Client\Unity\Output\android\ytpatch_zip");　　　　
        FileSystemInfo[] fileinfo = dir.GetFileSystemInfos(); //获取目录下（不包含子目录）的文件和子目录

        string szNewestPatch = "";
        Int64 nMaxTime = int.MinValue;　　　
        foreach (FileSystemInfo fileSystemInfo in fileinfo)
        {
            if (fileSystemInfo is DirectoryInfo) //判断是否文件夹
            { }
            else
            {
                string szFileName = fileSystemInfo.Name;
                if (szFileName.EndsWith("zip"))
                {
                    Int64 nTime = GetTime(szFileName);
                    if (nTime > nMaxTime)
                    {
                        szNewestPatch = szFileName;
                        nMaxTime = nTime;
                    }
                }
            }
        }
        if(szNewestPatch != "")
        {
            System.Console.WriteLine(szNewestPatch);
        }
    }
}