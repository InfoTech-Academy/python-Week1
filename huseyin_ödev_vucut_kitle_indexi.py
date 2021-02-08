print("Vücut Kitle İndex'i Hesaplama Programı")
Cevap="E"
while (Cevap=="E"):
    
    Boy=int(input("Lütfen Boyunuzu Giriniz(Cm): "))
    Kilo=float(input("Kilonuzu Giriniz: "))
    VKİ=Kilo/((Boy/100)**2)
    x=round(Kilo - 24.9 * ((Boy / 100) ** 2), 2)
    y=round(18.5*((Boy/100)**2)-Kilo,2)
    
    print("Vücut Kitle İndex'iniz {}".format(round(VKİ,2)))
    print("VKİ Sınıfınız: ")
    
    if VKİ <=18.5:
        print("Zayıf")
        print(f'{y} Kilo Almalısınız.')
        
    elif VKİ <=24.9:
        print("Normal")
        
    elif VKİ<=29.9:
        print("Fazla Kilolu")
        print(f'{x} Kilo Vermelisiniz.')
        
    elif VKİ<=34.9:
        print("Tip 1 Obez")
        print(f'{x} Kilo Vermelisiniz.')
        
    elif VKİ<=39.9:
        print("Tip 2 Obez")
        print(f'{x} Kilo Vermelisiniz.')

    else:
        print("Morbid Obez")
        print(f'{x} Kilo Vermelisiniz.')
        
    print("Devam etmek istiyormusunuz(E/H)?:")
    Cevap=input()
    
    while (True):
    
        if (Cevap=="E"):
            Cevap="E"
            print("Lütfen bekleyiniz...")
            break        
       
        elif (Cevap=="H"):
            break
    
        else:
            print("Yanlış bir iade girdiniz lütfen (E/H) ifadelerinden birini giriniz")
            Cevap = input()
            
                    
print("Sağlıklı Günler Dileriz.(Y)(Y)")       
        