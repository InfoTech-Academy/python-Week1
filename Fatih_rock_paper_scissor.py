count1=0
count2=0
i=1
user1_name=input("Please, enter your name as first player:")
user2_name=input("Please, enter your name as second player:")

while i<=10:
    print("Round: ", i)
    print(user1_name, end="")
    user1=input(", Please make your choice: Rock-Paper-Scissor ")
    print(user2_name, end="")
    user2=input(", Please make your choice: Rock-Paper-Scissor ")
    if user1.lower() == "rock":
        if user2.lower()=="rock":
            print(user1_name, ":", count1, "Vs", user2_name, ":", count2)
            print("No winner of round", i)
            i += 1
            continue
        elif user2.lower()=="paper":
            count2+=1
            print(user1_name, ":", count1, "Vs", user2_name, ":", count2)
            print(user2_name, "is winner of round", i)
            i+=1
            continue
        elif user2.lower()=="scissor":
            count1+=1
            print(user1_name, ":", count1, "Vs", user2_name, ":", count2)
            print(user1_name, "is winner of round", i)
            i+=1
            continue
    if user1.lower() == "paper":
        if user2.lower()=="paper":
            print(user1_name, ":", count1, "Vs", user2_name, ":", count2)
            print("No winner of round", i)
            i += 1
            continue
        elif user2.lower()=="rock":
            count1+=1
            print(user1_name, ":", count1, "Vs", user2_name, ":", count2)
            print(user1_name, "is winner of round", i)
            i+=1
            continue
        elif user2.lower()=="scissor":
            count2+=1
            print(user1_name, ":", count1, "Vs", user2_name, ":", count2)
            print(user2_name, "is winner of round", i)
            i+=1
            continue
    if user1.lower() == "scissor":
        if user2.lower()=="scissor":
            print(user1_name, ":", count1, "Vs", user2_name, ":", count2)
            print("No winner of round", i)
            i += 1
            continue
        elif user2.lower()=="paper":
            count1 += 1
            print(user1_name, ":", count1, "Vs", user2_name, ":", count2)
            print(user1_name, "is winner of round", i)

            i+=1
            continue
        elif user2.lower()=="rock":
            count2 += 1
            print(user1_name, ":", count1, "Vs", user2_name, ":", count2)
            print(user2_name, "is winner of round", i)

            i+=1
            continue
        else:
            print("You have a mistake! Please write your selection correctly")
    else:
        print("You have a mistake! Please write your selection correctly")

if count1>count2:
    print(user1_name, ":", count1, "Vs", user2_name, ":", count2)
    print("*********CONGRATULATIONS*********")
    print(user1_name, "beat", user2_name, "by", count1, ":", count2)
elif count1<count2:
    print(user1_name, ":", count1, "Vs", user2_name, ":", count2)
    print("*********CONGRATULATIONS*********")
    print(user2_name, "beat", user1_name, "by", count1, ":", count2)
else:
    print(user1_name, ":", count1, "Vs", user2_name, ":", count2)
    print("No winner of a match")
