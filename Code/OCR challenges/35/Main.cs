using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp
{
    class Program
    {
        public static int Game(int bal)
        {
            int bonus = 0 ;

            // Returns a random integer less than 30
            System.Random random = new System.Random(); 
            int ranNum = random.Next(31); 

            // User input, convert to int and validate
            int userInt = -1;
            while (userInt < 0 || userInt > 30){
                Console.WriteLine("Guess a number from 0 to 30");
                string user1 = Console.ReadLine();
                userInt = Int32.Parse(user1);
            }

            int userGamba = -1;
            while(userGamba < 0 || userGamba > bal){
                Console.WriteLine(string.Format("You have {0} money how much would you like to bet:",bal));
                string user2 = Console.ReadLine();
                userGamba = Int32.Parse(user2);
            }

            Console.WriteLine(string.Format("The correct number was {0}", ranNum));

            bal -= userGamba;

            // array of primes
            int[] primesArr = {1,2,3,5,7,11,13,17,19,23,29};

            // win conditions
            if(userInt == ranNum){
                bonus = 1;

                if (ranNum % 10 == 0){
                    bonus *= 3;
                }
                if (ranNum % 2 == 0){
                    bonus *= 2;
                }
                if (primesArr.Contains(ranNum)){
                    bonus *= 5;
                }
                if(ranNum < 6){
                    bonus *= 2;
                }
            }

            // outputs
            int winnings = userGamba * bonus;
            Console.WriteLine(string.Format("You won {0} money\n", winnings));

            return (bal+winnings);
        }

        static void Main(string[] args)
        {
            // as the game method is static, it doenst need to be instanced
            int bal = 50;
            while(bal > 0){
                bal = Program.Game(bal);
            }
        }
    }
}
