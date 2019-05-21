using System;
using System.Collections.Generic;
using System.IO;
using ICSharpCode.SharpZipLib.Zip;
using Newtonsoft.Json;
using TinyJson;

namespace YT
{

    public class PatchListFileInfo
    {
        public string m_szName;
        public uint m_uSize;
        public string m_szMD5;
        public string m_szAbName;
        public bool ParseFromLine(string szLine)
        {
            string[] listValue = szLine.Split(",");
            this.m_szName = listValue[0];
            this.m_uSize = uint.Parse(listValue[1]);
            this.m_szMD5 = listValue[2];
            this.m_szAbName = listValue[3];
            if (this.CheckValue())
            {
                return true;
            }
            else
            {
                Console.WriteLine("Error line:" + szLine);
                return false;
            }
        }
        public bool CheckValue()
        {
            bool bCheckOK = true;
            if (this.m_szName == "")
            {
                Console.WriteLine("Name is empty");
                bCheckOK = false;
            }
            if (this.m_uSize <= 0)
            {
                Console.WriteLine("Size is zero");
                bCheckOK = false;
            }
            if (this.m_szMD5 == "")
            {
                Console.WriteLine("MD5 is empty");
                bCheckOK = false;
            }
            if (this.m_szAbName == "")
            {
                Console.WriteLine("AbName is empty");
                bCheckOK = false;
            }

            return bCheckOK;

        }
    }
    public class PatchListDataTxt
    {
        // public string VersionCode;
        public List<PatchListFileInfo> m_ListPatchListFileInfo;

        public PatchListDataTxt()
        {
            m_ListPatchListFileInfo = new List<PatchListFileInfo>();
        }
        // public string playerName;
        public bool ParseFromFile(string szPatchFileName)
        {
            bool bParseFromFile = true;
            if (File.Exists(szPatchFileName))
            {
                PatchListDataTxt patchListData = new PatchListDataTxt();
                using(StreamReader sr = new StreamReader(szPatchFileName))
                {
                    while (!sr.EndOfStream)
                    {
                        string szLine = sr.ReadLine();
                        try
                        {
                            PatchListFileInfo patchListFileInfo = new PatchListFileInfo();
                            if (!patchListFileInfo.ParseFromLine(szLine))
                            {
                                bParseFromFile = false;
                            }
                            patchListData.m_ListPatchListFileInfo.Add(patchListFileInfo);
                        }
                        catch (Exception e)
                        {
                            Console.WriteLine("Exception Line format error:" + szLine);
                            return false;
                        }
                    }
                }
            }
            else
            {
                Console.WriteLine("FileNotFound:" + szPatchFileName);
                bParseFromFile = false;
            }

            return bParseFromFile;
        }
    }
    public class PatchListData
    {
        public string VersionCode;
        public List<List<string>> FileList;
        // public string playerName;
    }
    class HelloWorld
    {

        static void TestParseJson()
        {
            if (File.Exists("20180102_patchlist.json"))
            {
                using(StreamReader sr = new StreamReader("20180102_patchlist.json"))
                {

                    string szFileText = sr.ReadToEnd();
                    Console.WriteLine(szFileText);
                    PatchListData PatchListDataObj1 = szFileText.FromJson<PatchListData>();
                    Console.WriteLine("xjc");
                }
            }
        }
        static void main1()
        {
            string szMsg = "Hello World!";
            Console.WriteLine(szMsg);

            string szPatchFileName = "20180102_patchlist.txt";
            PatchListDataTxt patchListDataTxt = new PatchListDataTxt();
            if (patchListDataTxt.ParseFromFile(szPatchFileName))
            {
                Console.WriteLine("Parse From File True");
            }
            else
            {
                Console.WriteLine("Parse From File False");
            }
        }
        // static void Main(string[] args)
        // {
        //     Console.WriteLine("xjc");
        //     // string szSrc = @"F:/project/github/HelloWorld/c#/input";
        //     // using(ZipOutputStream zos = new ZipOutputStream(File.Create("output.zip")))
        //     // {
        //     //     zos.SetLevel(1); //不压缩
        //     //     string szPrefixRel = szSrc.Substring(0, szSrc.LastIndexOf('/') + 1);
        //     //     //string szPrefix = "output/";
        //     //     string szPrefix = "";
        //     //     Compress(szSrc, zos, szPrefix, szPrefixRel);
        //     // }
        //     Console.WriteLine("xjc".Substring(0,0));

        // }
        private static void Compress(string szSrc, ZipOutputStream s, string szPrefix, string szPrefixRel)
        {
            string[] filenames = Directory.GetFileSystemEntries(szSrc);
            foreach (string szFileT in filenames)
            {
                string szFile = szFileT.Replace("\\", "/");
                if (Directory.Exists(szFile))
                {
                    // 递归压缩子文件夹
                    Compress(szFile, s, szPrefix, szPrefixRel);
                }
                else
                {
                    using(FileStream fs = File.OpenRead(szFile))
                    {
                        byte[] buffer = new byte[4 * 1024];
                        string szZipEntryName = szFile.Replace(szPrefixRel, szPrefix);
                        ZipEntry entry = new ZipEntry(szZipEntryName);
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
            }
        }
    }
}