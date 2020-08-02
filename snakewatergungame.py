#snake water gun game

import random
list = ["s","w","g"]

chance = 10
no_of_chance = 0
computer_point = 0
human_point = 0
a= "Snake  , Water  , Gun Game "
print(a.center(200))


print(" s for snake")
print(" w for water")
print(" g for gun ")

while no_of_chance < chance:

    comp = random.choice(list)
    c = str(input("Enter your choice : "))
    human = c.lower()

    if comp == human:
        print("Tie each have 0 pt\n ")
        print(f"comp {computer_point} and human {human_point}")

    elif human =="s" and comp =="g":
        computer_point += 1
        print(f"your guess {human} and computer guess {comp}\n")
        print("Computer wins 1 point\n")
        print(f"Computer point is {computer_point} and your point is {human_point}\n")

    elif human == "s" and comp == "w":
        human_point += 1
        print(f"your guess {human} and computer guess {comp}\n")
        print("You wins 1 point\n")
        print(f"Computer point is {computer_point} and your point is {human_point}\n")

    elif human == "w" and comp == "s":
        computer_point += 1
        print(f"your guess {human} and computer guess {comp}\n")
        print("Computer wins 1 point\n")
        print(f"Computer point is {computer_point} and your point is {human_point}\n")


    elif human == "w" and comp == "g":
        human_point += 1
        print(f"your guess {human} and computer guess {comp}\n")
        print("You wins 1 point\n")
        print(f"Computer point is {computer_point} and your point is {human_point}\n")


    elif human == "g" and comp == "s":
        human_point += 1
        print(f"your guess {human} and computer guess {comp}\n")
        print("You wins 1 point\n")
        print(f"Computer point is {computer_point} and your point is {human_point}\n")


    elif human == "g" and comp == "w":
        computer_point += 1
        print(f"your guess {human} and computer guess {comp}\n")
        print("Computer wins 1 point\n")
        print(f"Computer point is {computer_point} and your point is {human_point}\n")


    else:
        print("You have entered wrong input\n")

    no_of_chance = no_of_chance +1
    print(f"{chance - no_of_chance} is left out of {chance}\n")

print("Game Over")

if computer_point == human_point:
    print("Tie")

elif computer_point > human_point:
    print("Conputer wins and you loose")

else:
    print("You win and computer loose")

print(f"Your point is {human_point} and computer point is {computer_point}")



