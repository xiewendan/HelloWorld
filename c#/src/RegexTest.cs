
using System;
using System.IO;
using System.Text.RegularExpressions;
public class RegexTest
{
    public static string GetMatchName()
    {
        string szPng = "Common_atlas0.png";
        string szReg = "[a-zA-Z0-9_]*(?=_atlas[0-9]+.png$)";
        string szRet = Regex.Match(szPng, szReg).Value;
        System.Console.WriteLine( szRet == "");
        return szRet;

        // foreach (Match match in Regex.Matches(szPng, szReg))
        // {
        //     System.Console.WriteLine(match.Captures[1]);
        //     match.
        //     if (match.Value.Length > 0)
        //     {
        //         return szPng.Substring(0, szPng.Length - match.Value.Length);
        //     }
        // }
    }
    public static bool IsMatch()
    {
        // string szShader = "E:\\project\\dm109\\tools\\GameEngine\\Client\\Unity\\Assets\\ArtRes\\Animations\\hero.meta";
        string szShader = "ArtRes/Characters/Boss/tlbb/duanyanqing/Materials/duanyanqin0100_d_001.mat";
        // string szReg = "[.*]\\.mat$|[.*]\\.shader$|[.*]\\.meta$";
        string szReg = ".*\\.meta$|^ArtRes/Characters/.*\\.mat$";
        return Regex.IsMatch(szShader, szReg);
    }
    public static void main()
    {
        System.Console.WriteLine(RegexTest.IsMatch());
    }
}