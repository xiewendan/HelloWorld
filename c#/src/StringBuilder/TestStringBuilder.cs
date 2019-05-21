/*
* __author__ = xiaobao
* __date__ = 2019/02/14 10:45:05
*
* desc: 测试一下 StringBuilder.append, string + string, string.Format("xjc", 111)
*/

using System.Text;
public class TestStringBuilder
{
    public static void main()
    {

        System.Diagnostics.Stopwatch StringBuilderStopwatch = new System.Diagnostics.Stopwatch();
        StringBuilderStopwatch.Start();
        {
            for(int i = 1; i < 1000; i++)
            {
                StringBuilder a = new StringBuilder("111");
                a.Append(i.ToString());
                a.Append("222");
                a.Append(1000.ToString());
                a.Append(1000.ToString());
                a.Append(1000.ToString());
                a.Append(1000.ToString());
            }
        }
        StringBuilderStopwatch.Stop();
        Debug.Log(string.Format("StringBuilderStopwatch xxx:{0}",StringBuilderStopwatch.Elapsed.TotalSeconds));


        System.Diagnostics.Stopwatch StringStopwatch = new System.Diagnostics.Stopwatch();
        StringStopwatch.Start();
        {
            for(int i = 1; i < 1000; i++)
            {
                string a = "111" + i.ToString() + "222" + 1000.ToString() + 1000.ToString() + 1000.ToString() + 1000.ToString();
            }
        }
        StringStopwatch.Stop();
        Debug.Log(string.Format("StringStopwatch xxx:{0}",StringStopwatch.Elapsed.TotalSeconds));


        System.Diagnostics.Stopwatch StringFormatStopwatch = new System.Diagnostics.Stopwatch();
        StringFormatStopwatch.Start();
        {
            for(int i = 1; i < 1000; i++)
            {
                string a = string.Format("111{0}{1}{2}{3}{4}{5}", i.ToString(), "222", 1000.ToString(), 1000.ToString(), 1000.ToString(), 1000.ToString());
            }
        }
        StringFormatStopwatch.Stop();
        Debug.Log(string.Format("StringFormatStopwatch xxx:{0}",StringFormatStopwatch.Elapsed.TotalSeconds));
    }
}