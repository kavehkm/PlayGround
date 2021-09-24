using System;

namespace Sharp
{
    class Loops
    {
        public static void ForLoop()
        {
            for (int i = 1; i <= 10; i++)
            {
                Console.WriteLine($"Value of i is {i}");
            }
        }

        public static void WhileLoop()
        {
            int counter = 1;

            while (counter <= 10)
            {
                Console.WriteLine($"Value of counter is {counter}");
                counter += 1;
            }
        }

        public static void ForeachLoop()
        {
            int[] marks = { 1, 2, 3, 4, 5, 6 };

            foreach (int mark in marks)
            {
                Console.WriteLine(mark);
            }
        }
    }
}
