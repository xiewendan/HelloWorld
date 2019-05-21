using System;
using System.IO;
using SimpleJSON;
public class TestSimpleJson
{
    public static void TestPrint()
    {

        string szJsonText = GetJsonText("src/SimpleJson/prefab_path_to_abname.json");
        if (szJsonText == "")
        {
            System.Console.WriteLine("Json path not found");
        }

        try
        {
            JSONNode objJsonNode = JSON.Parse(szJsonText);
            System.Console.WriteLine(objJsonNode.ToString(4));
            File.WriteAllText("src/SimpleJson/prefab_path_to_abname1.json", objJsonNode.ToString(4));
        }
        catch (System.Exception)
        {
            System.Console.WriteLine("json format error");
            throw;
        }

    }
    private static string GetJsonText(string szJsonPath)
    {
        if (File.Exists(szJsonPath))
        {
            return File.ReadAllText(szJsonPath);
        }

        return "";
    }
}