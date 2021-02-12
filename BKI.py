



while True:
    boy = float(input("Boyunuzu cm olarak giriniz : "))
    kilo = float(input("Kilonuzu kg olarak giriniz : "))
    bki = (kilo) / (boy * boy / 10000)

    if 0<bki and bki<18.4 :
         print("zayif")
    elif 18.5 < bki and bki<24.9:
         print("Normal")
    elif 25<bki and bki<29.9:
         print("fazla kilolu")
    elif 30<bki and 40>bki:
        print("obez")
    else:
         print("something wrong")

    condition= int(input("Devam edelim mi? (1 or 0)"))
    if condition==0:
        break