using System;

namespace Sharp
{
    class Variables
    {
        public static void Define()
        {
            int age = 27;

            float average = 18.75F;

            double pi = 3.14151617D;

            string firstName = "kaveh";

            string lastName = "Mehrbanian";

            bool strap = true;

            char ch = 'G';

            Console.WriteLine($"age: {age} | average: {average} | pi: {pi}");
            Console.WriteLine($"first name: {firstName} | last name: {lastName} | strap: {strap}");
            Console.WriteLine($"Bury Me a {ch}");
        }
    }
}
