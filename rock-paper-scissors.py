""""This program works as a classic rock-paper-scissor game between two participants"""

player_1=input("Please enter your name: ")
player_2=input("Please enter your name: ")
score_player_1, score_player_2 = 0, 0
round = 1
game_count = int(input("How many turn you want to play"))

def check_choices(ch):
       if ch == "rock" or ch =="paper" or ch == "scissors":
            return True
       else:
            return False

def check_winner(ch1, ch2):
    global score_player_1
    global score_player_2
    if ch1==ch2:
        print("Round:",round, "Draw")
    elif ch1=="rock" and ch2=="scissors":
        print("Round:",round, "winner is",player_1)
        score_player_1+=1

    elif ch1=="rock" and ch2=="paper":
        print("Round:",round, "winner is",player_2)
        score_player_2 += 1

    elif ch1=="scissors" and ch2=="rock":
        print("Round:",round, "winner is",player_2)
        score_player_2 += 1

    elif ch1=="scissors" and ch2=="paper":
        print("Round:",round, "winner is",player_1)
        score_player_1 += 1

    elif ch1=="paper" and ch2=="rock":
        print("Round:",round, "winner is",player_2)
        score_player_2 += 1

    elif ch1=="paper" and ch2=="scissors":
        print("Round:",round, "winner is",player_2)
        score_player_2 += 1

    else:
        print("Something is wrong")

while round<=game_count:

    while True:
        chc_plyr_1= input("Your choice Player 1: ",)
        if (check_choices(chc_plyr_1)):
           break
        else:
            print("Your coice is not valid Player 1!")

    while True:
        chc_plyr_2 = input("Your choice Player 2: ")
        if (check_choices(chc_plyr_2)):
            break
        else:
            print("Your coice is not valid Player 2!")
    check_winner(chc_plyr_1, chc_plyr_2)
    round+=1
print("******************************************")
print("you have completed", game_count, "games")
print("******************************************")

if score_player_1>score_player_2:
    print("Final winner is: ", player_1)
elif score_player_1<score_player_2:
    print("Final winneris : ", player_2)
elif score_player_1==score_player_2:
    print("It is a draw")
else:
    print("Something is wrong")