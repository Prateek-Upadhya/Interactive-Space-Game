using System;
using System.Collections.Generic;

namespace C_sharp
{

    class Wizard{

        public string name;
        public string favourite_spell;
        private int spellSlots;
        private float experience;

        public static int Count;


        public Wizard(string _name, string _favourite_spell){
            name = _name;
            favourite_spell = _favourite_spell;
            spellSlots = 2;
            experience = 0f;
            Count++;

        }

        public void CastSpell(){

            if(spellSlots > 0){
                Console.WriteLine("The Wizard " + name + " casts "+ favourite_spell);
                spellSlots--;
                experience += 0.3f;
            }
            else{
                Console.WriteLine("The wizard"+ name + " is out of spell slots.");
            }
        }

        public void Meditate(){

            Console.WriteLine(name + " wizard has decided to meditate.");
            spellSlots += 2;

        }


    }




    class Program
    {
        static void Main(string[] args){

            Wizard wiz1 = new Wizard("Harry Potter", "Expecto Patronum");
            Wizard wiz2 = new Wizard("Hermione Granger", "Occulo repairo");
            
            Console.WriteLine(Wizard.Count);
;    
        }
    }

}