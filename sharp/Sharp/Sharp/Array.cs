using System;

namespace Sharp
{
    class Array
    {
        static void PrintArray(int[] array)
        {
            foreach (int item in array)
            {
                Console.WriteLine(item);
            }
        }

        static void PrintArray(string[] array)
        {
            foreach (string item in array)
            {
                Console.WriteLine(item);
            }
        }

        public static void Define()
        {
            // array of int
            int[] marks = new int[10];

            // array of string
            string[] names = new string[5];

            // print arrays
            PrintArray(marks);
            PrintArray(names);
        }

        public static void DefineAndInitialize()
        {
            int[] marks = new int[] { 1, 2, 3, 4, 5 };

            string[] names = new string[5] { "kaveh", "amin", "ahmad", "mehran", "saeed" };

            // print arrays
            PrintArray(marks);
            PrintArray(names);
        }

        public static void Access()
        {
            string[] names = new string[5];

            names[0] = "kaveh";
            names[1] = "ahmad";
            names[2] = "amin";
            names[3] = "mehran";
            names[4] = "javad";

            for (int i = 0; i < names.Length; i++)
            {
                Console.WriteLine(names[i]);
            }

        }
    }
}
