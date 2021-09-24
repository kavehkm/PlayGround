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
        }
    }
}
