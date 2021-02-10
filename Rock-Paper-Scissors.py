"""
Oyuncularin adlarini alip tas - kagit - makas oyunu oynatiniz. 
Oyun 10 el surecektir. 10 el sonunda kazanan belli olacaktir. Skor sonucta gosterilecektir.
"""
player_1 = input("1. Oyuncunun ismini giriniz: ")
player_2 = input("2. Oyuncunun ismini giriniz: ")


player_1_score = 0
player_2_score = 0

game = 1
'''
taş > makas
makas > kağıt
kağıt > taş
'''
while (game < 11):

    player_1_sel = input("1. Oyuncu seçimi: taş/kağıt/makas? : ")
    player_2_sel = input("2. Oyuncu seçimi: taş/kağıt/makas? : ")

    if player_1_sel == "taş" and player_2_sel == "makas": #1 numara taş > 2 numara makas
        print(f"{player_1} {game} numaralı oyunu kazandı")
        player_1_score += 1
        print(f"skor: {player_1} = {player_1_score} {player_2} = {player_2_score}")
        game += 1
    elif player_2_sel == "taş" and player_1_sel == "makas": # 2 numara taş > 1 numara makas
        print(f"{player_2} {game} numaralı oyunu kazandı")
        player_2_score += 1
        print(f"skor: {player_1} = {player_1_score} {player_2} = {player_2_score}")
        game += 1
    elif player_1_sel == "makas" and player_2_sel == "kağıt": # 1 numara makas > 2 numara kağıt
        print(f"{player_1} {game} numaralı oyunu kazandı")
        player_1_score += 1
        print(f"skor: {player_1} = {player_1_score} {player_2} = {player_2_score}")
        game += 1
    elif player_1_sel == "kağıt" and player_2_sel == "makas": # 2 numara makas > 1 numara kağıt
        print(f"{player_2} {game} numaralı oyunu kazandı")
        player_2_score += 1
        print(f"skor: {player_1} = {player_1_score} {player_2} = {player_2_score}")
        game += 1
    elif player_1_sel == "kağıt" and player_2_sel == "taş": # 1 numara kağıt > 2 numara taş
        print(f"{player_1} {game} numaralı oyunu kazandı")
        player_1_score += 1
        print(f"skor: {player_1} = {player_1_score} {player_2} = {player_2_score}")
        game += 1
    elif player_1_sel == "taş" and player_2_sel == "kağıt": # 2 numara kağıt > 1 numara taş
        print(f"{player_2} {game} numaralı oyunu kazandı")
        player_2_score += 1
        print(f"skor: {player_1} = {player_1_score} {player_2} = {player_2_score}")
        game += 1
    elif player_1_sel == player_2_sel: # berabere
        print(f"{game} numaralı oyun berabere")
        print(f"skor: {player_1} = {player_1_score} {player_2} = {player_2_score}")
        game += 1

if player_1_score > player_2_score:
    print(f"Oyunu {player_1} kazandı")
elif player_2_score > player_1_score:
    print(f"Oyunu {player_2} kazandı")
else:
    print("oyun berabere")