# ======================================ROCK-PAPER-SCİSSORS================================================
# Developer: Cemil Tepecik
# Date:31.01.2021
# {This is a hand game usually played between two people, in which each player simultaneously forms one of three shapes with
# an outstretched hand. These shapes are "rock" (a closed fist), "paper" (a flat hand), and "scissors" (a fist with
# the index finger and middle finger extended, forming a V). "Scissors" is identical to the two-fingered V sign
# except that it is pointed horizontally instead of being held upright in the air.
# A simultaneous, zero-sum game, it has only two possible outcomes: a draw, or a win for one player and a loss for the other.
# Winner is determined by the rule: ...>rock>scissors>paper>rock>scissors>paper>...}
#===================================================================
#------------------INITIAL PART-----------------------------------
print("Welcome to Rock-Paper-Scissors Game! Good Luck...")
action_cluster=['1','2','3']
total_point_a = 0
total_point_b = 0

i=1
#---------------------MAIN PROGRAM------------------------------------
#----------------First Part: Take the Preferences-----------------------
while i<11:    # Totally 10
    print("If your action is Rock, enter 1")
    print("If your action is Paper, enter 2")
    print("If your action is Scissors, enter 3")

    # Take the choiese of Player A.........
    switch = '1'
    while switch == '1':
        print('Enter the Action of A...')
        actionA = input('Player A:')
        if actionA in action_cluster:
            action_PlayerA = str(actionA)
            switch = '2'
        else:
            print("Please enter a valid action!")

    # Take the choiese of Player A.........
    switch = '1'
    while switch == '1':
        print('Enter the Action of B...')
        actionB = input('Player B:')
        if actionB in action_cluster:
            action_PlayerB = str(actionB)
            switch = '2'
        else:
            print("Please enter a valid action!")

# ----------------Second Part: Determine the Winner-----------------------
    #Determine who wins int this tour.........
    point_a = 0
    point_b = 0

    #If B wins
    if action_PlayerA=='1' and action_PlayerB=='2':
        point_b=2
    if action_PlayerA=='2' and action_PlayerB=='3':
        point_b=2
    if action_PlayerA=='3' and action_PlayerB=='1':
        point_b=2

    # If A wins
    if action_PlayerB=='1' and action_PlayerA=='2':
        point_a=2
    if action_PlayerB=='2' and action_PlayerA=='3':
        point_a=2
    if action_PlayerB=='3' and action_PlayerA=='1':
        point_a=2

    # If the game ties
    if action_PlayerB==action_PlayerA:
        point_a=1
        point_b=1

    # Count the points for this tour
    total_point_a = int(total_point_a)+ int(point_a)
    total_point_b = int(total_point_b)+ int(point_b)
    print('point_a=', point_a, 'point_b=', point_b) # print the points of this tour
    print('Tour number:', i, 'of 10')   #print the tour of the game
    print('Point of Player A=', total_point_a) #print the total point of player A
    print('Point of Player B=', total_point_b) #print the total point of player B
    i=i+1 # turn to next tour.

# ------------FINAL PART OF THE PROGRAM: Determine and Declare the winner...................
if int(total_point_a) > total_point_b:
    print('Winner is... Player A')
if int(total_point_b) > total_point_a:
    print('Winner is... Player B')
if int(total_point_b)== total_point_a:
    print('No Winner... Player Are Ties !')
print('Player A:',total_point_a)
print('Player B:',total_point_b)
# -----------------------------------END--------------------------------------------------
#=========================================================================================
