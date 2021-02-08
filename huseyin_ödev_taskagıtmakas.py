
oypuan1 = 0   #Oyuncu1 Puanı
oypuan2 = 0   #Oyuncu2 Puanı


print(""" 1-->Taş\n 2-->Kağıt\n 3-->Makas""")

"""
Taş(1)      --Yener-->  Makas(3)
Kağıt(2)    --Yener-->  Taş(1)
Makas(3)    --Yener-->  Kağıt(2)
"""
i=0             #Tur 
while (i<=10):
    print("Kalan Tur Sayısı: {}".format(10-i))

    
    oyuncu1secim = int(input("Oyuncu1 Kararınız Nedir: "))    #1. Oyuncu1 dan seçimi alıyoruz
    oyuncu2secim = int(input("Oyuncu2 Kararınız Nedir: "))    #2. Oyuncu2 dan seçimi alıyoruz

    if(oyuncu1secim == 1):
        print("\n{}\t{}\n".format(oyuncu1secim,oyuncu2secim))
        if(oyuncu2secim == 1):     #Berabere
            print("Berabere, Skor Yazılmadı..")
        elif(oyuncu2secim == 2):   #Kazanan Oyuncu1
            oypuan1 = oypuan1 + 1
            print("Oyuncu1 Kazandı.. Oyuncu1 = {}, Oyuncu2 = {}".format(oypuan1,oypuan2))
            i = i + 1
        elif(oyuncu2secim == 3):   #Kazanan Oyuncu2
            oypuan2 = oypuan2 + 1
            print("Oyuncu2 Kazandı.. Oyuncu1 = {}, Oyuncu2 = {}".format(oypuan1,oypuan2))
            i = i + 1

    elif(oyuncu1secim == 2):
        print("\n{}\t{}\n".format(oyuncu1secim,oyuncu2secim))
        if (oyuncu2secim == 1):    #Kazanan Oyuncu2
            oypuan2 = oypuan2 + 1
            print("Oyuncu2 Kazandı.. Oyuncu1 = {}, Oyuncu2 = {}".format(oypuan1,oypuan2))
            i = i + 1
        elif (oyuncu2secim == 2):  #Berabere
            print("Berabere, Skor Yazılmadı..")
        elif (oyuncu2secim == 3):  #Kazanan Oyuncu1
            oypuan1 = oypuan1 + 1
            print("Oyuncu1 Kazandı.. Oyuncu1 = {}, Oyuncu2 = {}".format(oypuan1,oypuan2))
            i = i + 1

    elif (oyuncu1secim == 3):
        print("\n{}\t{}\n".format(oyuncu1secim,oyuncu2secim))
        if (oyuncu2secim == 1):    #Kazanan Oyuncu2
            oypuan2 = oypuan2 + 1
            print("Oyuncu2 Kazandı.. Oyuncu1 = {}, Oyuncu2 = {}".format(oypuan1,oypuan2))
            i = i + 1
        elif (oyuncu2secim == 2):  #Kazanan Oyuncu1
            oypuan1 = oypuan1 + 1
            print("Oyuncu1 Kazandı.. Oyuncu1 = {}, Oyuncu2 = {}".format(oypuan1,oypuan2))
            i = i + 1
        elif (oyuncu2secim == 3):  #Berabere
            print("Berabere, Skor Yazılmadı..")

    if(i == 10):
        print("Oyun Bitti..")
        print("Sonuçlar: Oyuncu1 = {}, Oyuncu2 = {}".format(oypuan1,oypuan2))
        break