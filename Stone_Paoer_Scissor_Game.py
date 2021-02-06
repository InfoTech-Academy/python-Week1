'''
Developer: Ersin ÖZTÜRK
Date: 01.02.2020
Purpose of Software: Reinforcement of learned Python Code and Self-improvement
What does program do? : This program is a Stone-Paper-Scissor Game.
Program takes a selection from player as Stone, Paper or Scissor.
And Computer select one of Stone, Paper or Scissor randomly.
This process repeats 10 times. The winner is the one who wins the most games.
'''

# "Import time" was used for computer random selection and for sleep function.
import time

game_counter=0
counter_of_computer_win=0
counter_of_player_win=0
name = input("\nPlease Insert Your Name:")
time.sleep(1)
print("Welcome "+name)
time.sleep(1)
print("\nPaper Stone Scissors Game Begins")
time.sleep(1)
print("==============================================")

# This while loop holds the game number.
while(game_counter < 10):


    # Local time is taken for each game. The second specified with "tm_sec".
    # "mod 10" of second is taken with mod mathematical operant.
    # The choice of computer is "stone" if the result is 0,3,6,9.
    # The choice of computer is "paper" if the result is 1,4,7.
    # The choice of computer is "scissor" if the result is 2,5,8.

    local_time=time.localtime()
    second_of_time=local_time.tm_sec
    mod_of_second=second_of_time%10

    if (mod_of_second==0 or mod_of_second==3 or mod_of_second==6 or mod_of_second==9):
        choice_of_computer= "stone"
    elif (mod_of_second==1 or mod_of_second==4 or mod_of_second==7):
        choice_of_computer = "paper"
    else:
        choice_of_computer = "scissor"


    #This while loop was used for understand if the selection is valid or not.

    while (True):
        time.sleep(2)
        option = input("Please insert      1 for STONE         2 for PAPER         3 for SCISSOR:      \n")

        if (option== "1"):
            choice_of_player= "stone"
            break
        elif (option == "2"):
            choice_of_player = "paper"
            break
        elif (option == "3"):
            choice_of_player = "scissor"
            break
        else:
            print("PLEASE MAKE A VALID CHOICE")
            continue

    # This "if block" was used for decide the winner.
    if(choice_of_player==choice_of_computer):

        winner= "equal"
    elif(choice_of_player == "stone" and choice_of_computer == "paper"):
        counter_of_computer_win += 1
        winner = "computer"
    elif(choice_of_player == "stone" and choice_of_computer == "scissor"):
        counter_of_player_win += 1
        winner = name
    elif (choice_of_player == "paper" and choice_of_computer == "stone"):
        counter_of_player_win += 1
        winner = name
    elif (choice_of_player == "paper" and choice_of_computer == "scissor"):
        counter_of_computer_win += 1
        winner = "computer"
    elif (choice_of_player == "scissor" and choice_of_computer == "stone"):
        counter_of_computer_win += 1
        winner = "computer"
    else:
        counter_of_player_win += 1
        winner = name

    time.sleep(2)

# The results was printed in detailed.
    print("\nChoice of Computer: " + choice_of_computer)
    print("\nChoice of Player: " + choice_of_player)
    print("")

    time.sleep(2)
    if (winner== "equal"):
       print(str(game_counter + 1) + ". Game is equal\n")
    else:
        print(str(game_counter + 1) + ". Game was won by " + str(winner)+" \n")

    game_counter+=1

print("=========GAME OVER==============")
print("=================================\n")
time.sleep(1)

print(str(counter_of_computer_win) + " times computer won")
time.sleep(1)

print(str(counter_of_player_win) + " times " + name + " won")
time.sleep(1)

print(str(10 - counter_of_player_win - counter_of_computer_win) + " times was equal")
time.sleep(1)
print("========RESULT=============")
time.sleep(1)
if (counter_of_computer_win>counter_of_player_win):

    print("Unfortunatelly COMPUTER WON")
elif (counter_of_player_win > counter_of_computer_win):

    print("CONGRATULATIONS!!! "+name+" won")
else:
    print("You were equal to Computer")