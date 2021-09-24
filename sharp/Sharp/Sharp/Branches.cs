using System;

namespace Sharp
{
    class Branches
    {
        static int userInput()
        {
            Console.WriteLine("Mark? ");

            string userInput = Console.ReadLine();

            return Convert.ToInt32(userInput);
        }

        public static void If()
        {
            int mark = userInput();

            if (mark > 18)
            {
                Console.WriteLine("Excellent");
            }
        }

        public static void IfElse()
        {
            int mark = userInput();

            if (mark > 18)
            {
                Console.WriteLine("Excellent");
            }
            else
            {
                Console.WriteLine("Bad");
            }
        }

        public static void IfElseIf()
        {
            int mark = userInput();

            if (mark > 18)
            {
                Console.WriteLine("Excellent");
            }
            else if (mark > 15)
            {
                Console.WriteLine("Hmmm");
            }
            else
            {
                Console.WriteLine("Bad");
            }
        }
    }
}
