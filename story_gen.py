import os
import time
def slp(tim):
    time.sleep(tim)
    return
print("Hello to this story generator game!\n")
slp(1.5)
print("in this game we are going to generate a story for you, we just need to ask you few questions\n")
slp(2.5)

name = input("What is character's name?\n")
print("Nice name!")
slp(1)
city = input("what city does your character live?\n")
print("Best people live in", city, "!")
while True:
    try:
        age = int(input("enter the character's age\n"))
    except ValueError:
        print("please insert a valid number.")
        continue
    else:
        break
print("your character is", age, "years old")
fac = input("what is your character's faction? Delta (ice guys) or Falcon (fire guys)\n")
if fac != "Delta" and fac != "Falcon":
    print("please enter a valid faction")
    exit()
print("your character is a member of", fac, "faction")
slp(1)
print("generating story...")
slp(5)
os.system('cls')
###########
if age < 20 and fac == "Delta":
    print("Your character is a young", fac, "member, he lives in", city, "and his name is", name, ".\n")
    slp(3.5)
    print("he likes to play with Ice and prove himself to be the best in his faction, one day a great dragon attacked "
          "the city, so he decied to fight with his city to defend it.\n")
    slp(8)
    print("however he was quite young so they didn't want to let him fight")
    slp(8)
    print("it was a disaster, the dragon killed many people and destroyed most of the city, the city asked for help "
          "from the rest of the faction, but they didn't get a response.\n")
    slp(8)
    print("so in last attempt to survive the attack, the people of the city left to another city, the city of", city, "was no more but history.")
    slp(8)
    print("years has passed since then, and people forgot about" , city, "and the dragon, they now live in peace in "
                                                                         "another city.")
    slp(8)
    print("the end.")
###########
elif age < 20 and fac == "Falcon":
    print("Your character is a young", fac, "member, he lives in", city, "and his name is", name, ".\n")
    slp(3.5)
    print("he likes to play with fire and prove himself to be the best in his faction, one day a great dragon "
          "attacked the city, so he decied to fight with his city to defend it.\n")
    slp(8)
    print("however he was quite young so they didn't want to let him fight")
    slp(8)
    print("it was a disaster, the dragon killed many people and destroyed most of the city, the city asked for help "
          "from the rest of the faction, but they didn't get a response.\n")
    slp(8)
    print("so in last attempt to survive the attack, the people of the city left to another city, the city of", city, "was no more but history.")
    slp(8)
    print("years has passed since then, and people forgot about" , city, "and the dragon, they now live in peace in "
                                                                         "another city.")
    slp(8)
    print("the end.")
###########
elif age > 20 and age < 50 and fac == "Delta":
    print("Your character is a", fac, "member, he lives in", city, "and his name is", name, ".\n")
    slp(3.5)
    print("he had a lot of friends, and he was looking to become a leader one day, one day a great dragon attacked "
          "the city, so he decided to fight with his city to defend it.\n")
    slp(8)
    print("he was a great warrior, he fought with the dragon and killed it, he saved the city and the people of the "
          "city were so happy that they made him the leader of the city.\n")
    slp(8)
    print("he was the best leader the city has ever had, he made the city the best city in the world\n")
    slp(8)
    print("the end.")
###########
elif age > 55 and fac == "Delta":
    print("Your character is a", fac, "member, he lives in", city, "and his name is", name, ".\n")
    slp(3.5)
    print("he was quite old and couldn't fight that much like before, but he was looking to become a leader one day, "
          "one day a great dragon attacked the city, so he decied to fight with his city to defend it.\n")
    slp(8)
    print("he was a great warrior, he fought with the dragon but he couldn't kill it, he and his friends couldn't "
          "get the dragon off their city, and most of the city were destroyed")
    slp(8)
    print("the city asked for help from the rest of the faction, and they came for help\n")
    slp(8)
    print("they killed the dragon and saved the city, they made him the leader of the city for his efforts in saving "
          "the city, he did the best among everyone else.\n")
    slp(8)
    print("the city of", city, "became a great economic center for the world to see, and they now live peacefully and "
                               "happily ever after.")
    slp(8)
    print("the end.")
###########
elif age > 20 and age < 50 and fac == "Falcon":
    print("Your character is a", fac, "member, he lives in", city, "and his name is", name, ".\n")
    slp(3.5)
    print("he had a lot of friends, and he was looking to become a leader one day, one day a great dragon attacked "
          "the city, so he decided to fight with his city to defend it.\n")
    slp(8)
    print("he was a great warrior, he fought with the dragon and killed it, he saved the city and the people of the "
          "city were so happy that they made him the leader of the city.\n")
    slp(8)
    print("he was the best leader the city has ever had, he made the city the best city in the world")
    slp(8)
    print("the end.")
###########
elif age > 55 and fac == "Falcon":
    print("Your character is a", fac, "member, he lives in", city, "and his name is", name, ".\n")
    slp(3.5)
    print("he was quite old and couldn't fight that much like before, but he was looking to become a leader one day, "
          "one day a great dragon attacked the city, so he decied to fight with his city to defend it.\n")
    slp(8)
    print("he was a great warrior, he fought with the dragon but he couldn't kill it, he and his friends couldn't "
          "get the dragon off their city, and most of the city were destroyed")
    slp(8)
    print("the city asked for help from the rest of the faction, and they came for help\n")
    slp(8)
    print("they killed the dragon and saved the city, they made him the leader of the city for his efforts in saving "
          "the city, he did the best among everyone else.\n")
    slp(8)
    print("the city of", city, "became a great economic center for the world to see, and they now live peacefully and "
                               "happily ever after.")
    slp(8)
    print("the end.")