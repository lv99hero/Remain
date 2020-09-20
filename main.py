import time
import sys
from termcolor import colored, cprint

def delay_print1(text): ## This will display text at .1 delay
  for c in text:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.1)
def delay_print2(text): ## This will display text at .25 delay
  for c in text:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.25)
def delay_print3(text): ## This will display text with a .05 delay
  for c in text:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.05)
def flash(text):
  for c in text:
    input(cprint(text, attrs=['blink']))


mylist = []

def beginnings(): ### Beginning questions for your class ###
  clist = ["Heavy Armor", "Medium Armor", "Spear", "Armorer", "Axe", "Blunt Weapon", "Long Blade", "Block", "Athletics"]
  slist = ["Acrobatics", "Light Armor", "Bow", "Sneak", "Hand-To-Hand", "Short Blade", "Mercantile", "Speechcraft"]
  mlist = ["Unarmored", "Illusion", "Alchemy", "Conjuration", "Enchant", "Alteration", "Destruction", "Mysticism", "Restoration"]
  #### This is to choose 3 physical skills ####

  delay_print3("""You open your eyes, and see nothing but a pitch black abyss.\nYou try to move your limbs to no success.\nYou listen, and there is no sound.\nHow long have you been here?\nWhere is "here"?\n\n""")
  time.sleep(2)
  delay_print3("""You remember your childhood.\nYour parents did your best to raise you,\ndespite the challenges.\nYou had friends.\n""")
  time.sleep(1)
  delay_print2("""You had friends.\n\n""")
  time.sleep(2)
  delay_print3("""You remember going to school, attending classes.\nYou did your best to make your parents proud.\nYour father wasn't around much.\nHe had to help keep the town safe.\n""")
  time.sleep(1)
  delay_print2("He had to keep ")
  delay_print1("YOU ")
  delay_print2("safe.\n")
  time.sleep(2)
  delay_print2("You recall him speaking at meal time.\nHe always had the best stories.\n\nWhat 3 skills did your father speak about again?\n\n")


  while len(clist) >= 7:

    for x in clist:
      print(colored(x, 'red'))

    c_choice = input()

    if c_choice in clist:
      print("\nDefinitely, it was " + c_choice)
      mylist.append(c_choice)
      clist.remove(c_choice)
      print("Your skills are as follows:\n ")
      for x in mylist:
        print(colored(x, 'green'))
    else:
      print("That's no good.")

  #### This is to choose 3 stealth skills ####
  while len(slist) >= 6:

    for x in slist:
      print(colored(x, 'yellow'))

    s_choice = input(str("\n\nWhat will your 3 major stealth skills be?\n\n"))

    if s_choice in slist:
      print("\nThat works fine!")
      mylist.append(s_choice)
      slist.remove(s_choice)
      print("Your skills are as follows:\n ")
      for x in mylist:
        print(colored(x, 'green'))
    else:
      print("That's no good.")
  #### This is to choose 3 magical skills ####

  while len(mlist) >= 7:

    for x in mlist:
      print(colored(x, 'magenta'))

    m_choice = input(str("\n\nWhat will your 3 major magical skills be?\n\n"))

    if m_choice in mlist:
      print("\nThat works fine!")
      mylist.append(m_choice)
      mlist.remove(m_choice)
      print("Your skills are as follows:\n ")
      for x in mylist:
        print(colored(x, 'green'))
    else:
      print("That's no good.")

    if len(mylist) == 9:

      print("Your classes are as follows: /n")
      for x in mylist:
        print (colored(x, 'green'))

        confirm = input("This seems to be your choices. Do you accept? Y/N\n")
        if confirm == "Y" or "n":
          SystemExit
        elif confirm == "N" or "n":
          SystemExit
        else:
          delay_print3("That's not valid. Try again.")

def prologue():
  delay_print3("You ")


(delay_print1("""“The true soldier fights not\n\t because he hates what is in front of him, \n\t\tbut because he loves what is behind him."\n\n"""))
(delay_print2("-G.K. Chesterton\n"))
time.sleep(2)

beginnings()