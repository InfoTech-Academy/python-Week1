import random

user1 = input("Enter User1 name?\n")
user2 = input("Enter User2 name?\n")
a = ["tas", "kagit","makas"]

not1 = 0
not2 = 0
for x in range(1,11):
    pc1 = random.choice(a)
    pc2 = random.choice(a)

    if pc1 == pc2:
        continue
    elif pc1 == "tas":
        if pc2 == 'makas':
            not1 += 1
        else:
            not2 += 1
    elif pc1 == "kagit":
        if pc2 == 'makas':
            not2 += 1
        else:
            not1 += 1
    elif pc1 == "makas":
        if pc2 == 'kagit':
            not1 += 1
        else:
            not2 += 1

print(user1.capitalize(), not1, ",",user2.capitalize(), not2,"kez kazandi")
