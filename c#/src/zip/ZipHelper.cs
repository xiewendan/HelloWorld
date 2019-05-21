using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using ICSharpCode.SharpZipLib.Zip;

// 1、压缩文件成一个zip
// 2、从一个zip文件解压缩

public class Debug
{
    static public void Log(string szMsg)
    {
        System.Console.WriteLine(szMsg);
    }
}

public class ZipHelper
{
    public delegate bool FilterFun(string szStr);

    ///<summary>
    /// 压缩文件夹。
    /// 文件夹1
    /// 压缩成如下目录结构
    /// xxx.zip
    ///    szRootPathInZip
    ///         文件夹1下的文件和文件夹
    ///</summary>
    public static void Compress(string szSrcDir, string szDestZip, string szRootPathInZip, FilterFun filterFun = null)
    {
        if (!(szSrcDir.EndsWith("/") || szSrcDir.EndsWith("\\")))
        {
            szSrcDir += "/";
        }
        if (szRootPathInZip != "" && !(szRootPathInZip.EndsWith("/") || szRootPathInZip.EndsWith("\\")))
        {
            szRootPathInZip += "/";
        }

        if (!Directory.Exists(szSrcDir))
        {
            Debug.Log("compress failed, src path not exist:" + szSrcDir);
            return;
        }

        if (File.Exists(szDestZip))
        {
            Debug.Log("compress failed, output file exist:" + szDestZip);
            return;
        }

        using(ZipOutputStream zos = new ZipOutputStream(File.Create(szDestZip)))
        {
            zos.SetLevel(1); //不压缩
            string szRootDirOfSrc = szSrcDir;
            ZipHelper.Compress(szSrcDir, zos, szRootDirOfSrc, szRootPathInZip, filterFun);
        }
    }
    protected static void Compress(string szSrc, ZipOutputStream s, string szRootDirOfSrc, string szRootPathInZip, FilterFun filterFun = null)
    {
        Debug.Log("Compress, Src:" + szSrc + ", oldprefix: " + szRootDirOfSrc + ", newprefix: " + szRootPathInZip);

        string[] filenames = Directory.GetFileSystemEntries(szSrc);
        foreach (string szFileT in filenames)
        {
            string szFile = szFileT.Replace("\\", "/");
            if (Directory.Exists(szFile))
            {
                // 递归压缩子文件夹
                Compress(szFile, s, szRootDirOfSrc, szRootPathInZip);
            }
            else
            {
                string szFilePathInZip = szFile.Replace(szRootDirOfSrc, szRootPathInZip);
                if (filterFun == null || filterFun(szFile))
                {
                    CompressFile(szFile, s, szFilePathInZip);
                }
            }
        }
    }

    private static void CompressFile(string szFile, ZipOutputStream s, string szFilePathInZip)
    {
        if (!File.Exists(szFile))
        {
            Debug.Log("compress file failed, file not exist:" + szFile);
            return;
        }

        using(FileStream fs = File.OpenRead(szFile))
        {
            byte[] buffer = new byte[4 * 1024];
            ZipEntry entry = new ZipEntry(szFilePathInZip);
            entry.DateTime = DateTime.Now;
            s.PutNextEntry(entry);
            int sourceBytes;
            do
            {
                sourceBytes = fs.Read(buffer, 0, buffer.Length);
                s.Write(buffer, 0, sourceBytes);
            } while (sourceBytes > 0);
        }
    }

    /// <summary>
    /// 解压缩
    /// </summary>
    /// <param name="szZipFile ">压缩包完整路径地址</param>
    /// <param name="szDestDir ">解压路径是哪里</param>
    /// <returns></returns>
    public static bool Decompress(string szZipFile, string szRootDirInZip, string szDestDir, bool bIgnoreRoot)
    {
        if (szRootDirInZip != "" && !(szRootDirInZip.EndsWith("/") || szRootDirInZip.EndsWith("\\")))
        {
            szRootDirInZip += "\\";
        }
        szRootDirInZip = szRootDirInZip.Replace("/", "\\");

        if (!File.Exists(szZipFile))
        {
            throw new FileNotFoundException(string.Format("未能找到文件 '{0}'", szZipFile));
        }
        if (!Directory.Exists(szDestDir))
        {
            Directory.CreateDirectory(szDestDir);
        }

        bool bReplaceRootDirInZip = szRootDirInZip.Length > 0;
        using(var s = new ZipInputStream(File.OpenRead(szZipFile)))
        {
            ZipEntry theEntry;
            while ((theEntry = s.GetNextEntry()) != null)
            {
                if (theEntry.IsDirectory)
                {
                    continue;
                }

                string szSubPathInZip = theEntry.Name;
                szSubPathInZip = szSubPathInZip.Replace("\\", "/");
                if(bIgnoreRoot)
                {
                    int nIndex = szSubPathInZip.IndexOf("/");
                    if( nIndex > 0)
                    {
                        szSubPathInZip = szSubPathInZip.Substring(nIndex + 1);
                    }
                }

                string szSubDirInZip = Path.GetDirectoryName(szSubPathInZip);

                if (bReplaceRootDirInZip)
                {
                    szSubDirInZip = szSubDirInZip.Replace(szRootDirInZip, ""); // 如果根目录不为空，才需要替换
                }

                string szDirectorName = Path.Combine(szDestDir, szSubDirInZip);
                string szFileName = Path.Combine(szDirectorName, Path.GetFileName(theEntry.Name));
                // System.Console.WriteLine(szFileName);
                if (!Directory.Exists(szDirectorName))
                {
                    Directory.CreateDirectory(szDirectorName);
                }
                if (!String.IsNullOrEmpty(szFileName))
                {
                    using(FileStream streamWriter = File.Create(szFileName))
                    {
                        int size = 4096;
                        byte[] data = new byte[size];
                        while (size > 0)
                        {
                            size = s.Read(data, 0, data.Length);
                            streamWriter.Write(data, 0, size);
                        }
                    }
                }
            }
        }
        return true;
    }
    // static public void Main(string[] args)
    // {
    //     // 必须加，否则会爆code page 936找不到
    //     System.Text.Encoding.RegisterProvider(System.Text.CodePagesEncodingProvider.Instance);

    //     // System.Console.WriteLine("xjc");
    //     // string szSrcPath = @"F:/project/github/HelloWorld/c#/src/zip/Data";
    //     // string szDestZip = @"F:/project/github/HelloWorld/c#/src/zip/Output.zip";
    //     // if (File.Exists(szDestZip))
    //     // {
    //     //     File.Delete(szDestZip);
    //     // }
    //     // ZipHelper.Compress(szSrcPath, szDestZip, "");
    //     // System.Console.WriteLine("Finished");

    //     // string szDestDir = @"F:/project/github/HelloWorld/c#/src/zip/Data1";
    //     // string szRootDirInZip = @"Data\Data\";
    //     // ZipHelper.Decompress(szDestZip, szRootDirInZip, szDestDir);

    //     // 测试解压指定文件
    //     string szDestZip = @"F:/project/github/HelloWorld/c#/src/zip/Output1.zip";
    //     string szDestDir = @"F:/project/github/HelloWorld/c#/src/zip/Data1";
    //     string szRootDirInZip = @"";
    //     ZipHelper.Decompress(szDestZip, szRootDirInZip, szDestDir, true);

    //     System.Console.WriteLine("Main Start");
    // }
}