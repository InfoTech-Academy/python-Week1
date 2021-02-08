import random

number = random.randint(0, 2)

print("Well Come  Rock-Paper-Scissors game.\nThis game will continue 10 times ")

player1 = 0
player2 = 0
equation = 0
name1 = input("Write the first players name: ")
name2 = input("Write the first players name: ")
for i in range(0, 10):
    first = random.randint(0, 2)
    second = random.randint(0, 2)
    if first == second:
        equation += 1
    elif first == 0 and second == 1:
        player2 += 1
    elif first == 0 and second == 2:
        player1 += 1
    elif first == 1 and second == 2:
        player2 += 1
    elif first == 1 and second == 0:
        player1 += 1
    elif first == 2 and second == 0:
        player2 += 1
    elif first == 2 and second == 1:
        player1 += 1
    else:
        print("Something gone wrong")
print(name1 + " won " + str(player1) + " games \n" + name2 + " won "+str(player2)+" games \n" +
      str(equation) + " Games end in draw")

if player1 > player2:
    print(name1 + " Won The Game")
elif player2 > player1:
    print(name2 + " Won The Game")
else:
    print(" Game ends in Draw")
