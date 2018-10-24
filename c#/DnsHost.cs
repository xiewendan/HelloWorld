using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Text;

namespace GetHostNameUsingIP
{
    class Program
    {
        public static string GetLocalIp()
        {
            IPAddress localIp = null;

            try
            {
                IPAddress[] ipArray;
                ipArray = Dns.GetHostAddresses(Dns.GetHostName());
                localIp = ipArray.First(ip => ip.AddressFamily == System.Net.Sockets.AddressFamily.InterNetwork);
            }
            catch (Exception ex) { }
            if (localIp == null)
            {
                localIp = IPAddress.Parse("127.0.0.1");
            }
            return localIp.ToString();
        }

        static void Main(string[] args)
        {
            // string IPAdd = "204.79.197.200";  
            IPAddress IPAdd = IPAddress.Parse("10.254.251.45");
            // string IPAdd = "10.249.81.197";
            string szHostName = "default";
            try
            {
                IPHostEntry hostEntry = Dns.GetHostEntry(IPAdd);
                szHostName = hostEntry.HostName;
            }
            catch (System.Exception)
            {
                // throw;
            }

            Console.WriteLine(szHostName);

            Console.WriteLine(GetLocalIp());
        }
    }
}