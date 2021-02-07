# TAŞ KAĞIT MAKAS OYUNU
print("Taş, Kağıt, Makas Oyunu")
print("10 Elde Biter")
oyuncu1 = input("1.Oyuncunun İsmi : ")
oyuncu2 = input("2. Oyuncunun İsmi : ")
skor1 = 0
skor2 = 0
beraberlik = 0
i = 1
while (skor2 + skor1 + beraberlik + 1) <= 10:
    print("El Sayısı : ", i)
    print(oyuncu1, end=" ")
    cevap1 = input("Taş mı, Kağıt mı Yoksa Makas mı : ")
    print(oyuncu2, end=" ")
    cevap2 = input("Taş mı, Kağıt mı Yoksa Makas mı : ")
    if (skor2 + skor1 + beraberlik + 1) < 10:
        if (cevap1 != "Taş") and (cevap1 != "Kağıt") and (cevap1 != "Makas"):
            print(oyuncu1, ",", "Lütfen Taş, Kağıt, Makas' ten Birini Seçiniz...Bu Eli Yeniden Başlatıyorum")
            continue
        elif (cevap2 != "Taş") and (cevap2 != "Kağıt") and (cevap2 != "Makas"):
            print(oyuncu2, ",", "Lütfen Taş, Kağıt, Makas' ten Birini Seçiniz...Bu Eli Yeniden Başlatıyorum")
            continue
        elif ((cevap1 == "Taş" and cevap2 == "Taş") or (cevap1 == "Kağıt" and cevap2 == "Kağıt") or (
                cevap1 == "Makas" and cevap2 == "Makas")):
            print("Aynı Cevabı Seçerek Berabere Kaldınız", oyuncu1, "=", skor1, " , ", oyuncu2, "=", skor2)
            beraberlik += 1
            i += 1
            continue
        elif ((cevap1 == "Taş" and cevap2 == "Makas") or (cevap1 == "Kağıt" and cevap2 == "Taş") or (
                cevap1 == "Makas" and cevap2 == "Kağıt")):
            skor1 += 1
            i += 1
            print(oyuncu1, "Kazandı. Skor", oyuncu1, "=", skor1, " , ", oyuncu2, "=", skor2)
            continue
        else:
            skor2 += 1
            i += 1
            print(oyuncu2, "Kazandı. Skor", oyuncu1, "=", skor1, " , ", oyuncu2, "=", skor2)
            continue
    else:
        print("Oyun Bitti. 10 El Sonunda Kazanan...")
        if skor2 < skor1:
            print(oyuncu1)
            break
        elif skor1 == skor2:
            print("Yok. Berabere Kaldınız.")
            break
        else:
            print(oyuncu2)
            break
