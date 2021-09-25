using System;

namespace Sharp
{
    class Program
    {
        static void Main(string[] args)
        {
            // hello world
            HelloWorld.Message();


            // variables
            Variables.Define();


            // branches
            Branches.If();
            Branches.IfElse();
            Branches.IfElseIf();
            Branches.Swithch();


            // loops
            Loops.ForLoop();
            Loops.WhileLoop();
            Loops.ForeachLoop();

            // array
            Array.Define();
            Array.DefineAndInitialize();
            Array.Access();

            // classes
            Account account1 = new Account(1, "kaveh", "mehrbanian", 100);
            Console.WriteLine($"account1: {account1.id}, {account1.firstName}, {account1.lastName}, {account1.GetBalance()}");
            account1.Variz(1000);
            account1.Bardasht(600);
            Console.WriteLine($"accont1's balance after operations is {account1.GetBalance()}");
            // - working with properties
            Account1 account2 = new Account1(2, "mehran", "falahaty");
            account2.Balance = 1000;
            Console.WriteLine(account2.Balance);
        }
    }
}
