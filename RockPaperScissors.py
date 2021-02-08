#Furkan Surucu

import random
oyun_sayisi = 0
oyuncu_puani, bilgisayar_puani, beraberlik = 0,0,0
tkm= ["tas","kagit","makas"]

print("-"*5,"Tas, Kagit, Makas oyununa hosgeldiniz!","-"*5)
oyuncu= input("Adinizi giriniz: ")
while oyun_sayisi < 10:
    oyuncu_secim = input("tas, kagit, makas seciniz: ")
    oyuncu_secim = oyuncu_secim.lower()
    bilgisayar = random.choice(tkm)
    print("Rakip",bilgisayar, "secti")

    if oyuncu_secim == "tas":
        if bilgisayar == "tas":
            print("Dostluk kazandi..")
            beraberlik+=1
        elif bilgisayar == "kagit":
            print("Bilgisayar kazandi")
            bilgisayar_puani+=1
        else:
            print(oyuncu,"kazandi")
            oyuncu_puani +=1

    elif oyuncu_secim == "kagit":
        if bilgisayar == "kagit":
            print("Dostluk kazandi..")
            beraberlik+=1
        elif bilgisayar == "makas":
            print("Bilgisayar kazandi")
            bilgisayar_puani+=1
        else:
            print(oyuncu,"kazandi")
            oyuncu_puani += 1

    elif oyuncu_secim == "makas":
        if bilgisayar == "makas":
            print("Dostluk kazandi..")
            beraberlik+=1
        elif bilgisayar == "tas":
            print("Bilgisayar kazandi")
            bilgisayar_puani+=1
        else:
            print(oyuncu,"kazandi")
            oyuncu_puani += 1

    else:
        print("Lutfen gecerli bir giris yapin..")
        continue
    oyun_sayisi +=1
print("10 oyun sonunda:\n", oyuncu+":", oyuncu_puani,"\n Bilgisayar:", bilgisayar_puani, "\n Beraberlik:", beraberlik )
if oyuncu_puani > bilgisayar_puani:
    print(oyuncu, "Kazandi")
elif bilgisayar_puani > oyuncu_puani:
    print("Bilgisayar Kazandi")
else:
    print("Dostluk kazandi.")










