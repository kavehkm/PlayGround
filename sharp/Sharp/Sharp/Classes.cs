using System;

namespace Sharp
{
    class Account
    {
        public int id;
        public string firstName;
        public string lastName;
        private int balance;

        public Account(int id, string firstName, string lastName, int balance = 0)
        {
            this.id = id;
            this.firstName = firstName;
            this.lastName = lastName;
            this.balance = balance;
        }

        public int GetBalance()
        {
            return balance;
        }

        public void Variz(int value)
        {
            if (value < 0)
            {
                throw new Exception("Invalid value");
            }
            balance += value;
        }

        public void Bardasht(int value)
        {
            if (value < 0)
            {
                throw new Exception("Invalid value");
            }

            // compute remain
            int remain = balance - value;

            if (remain < 0)
            {
                throw new Exception("Not enough balance");
            }

            balance = remain;
        }
    }

    class Account1
    {
        public int id;
        public string firstName;
        public string lastName;
        private int balance;

        public Account1(int id, string firstName, string lastName, int balance = 0)
        {
            this.id = id;
            this.firstName = firstName;
            this.lastName = lastName;
            this.balance = balance;
        }

        public int Balance
        {
            get
            {
                return balance;
            }
            set
            {
                if (value < 0)
                {
                    throw new Exception("Invalid value");
                }
                balance = value;
            }
        }
    }

    class Animal
    {
        public string name;

        public Animal(string name)
        {
            this.name = name;
        }

        public virtual void MakeSound()
        {
            Console.WriteLine("Animal Sound");
        }

        public virtual void Sleep()
        {
            Console.WriteLine("ZzzzZzzz");
        }
    }

    class Dog : Animal
    {
        public string breed;

        public Dog(string name, string breed) : base(name)
        {
            this.name = name;
            this.breed = breed;
        }
        public override void MakeSound()
        {
            Console.WriteLine("Hop Hop Bow Bows");
        }

        public override void Sleep()
        {
            base.Sleep();
            Console.WriteLine("WWwwwWW...");
        }
    }
}
