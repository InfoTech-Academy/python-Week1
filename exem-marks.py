adiniz=input("Adinizi Giriniz")
soyadiniz=input("Soyadinizi Giriniz")
ogrenciNo=input("Ogrenci Numaranizi Giriniz")

for i in range(1,5):
    ders=(input(f"{i} dersin adini giriniz"))
    vize=int(input(f"{i} dersin vize notunu giriniz"))
    final=int(input(f"{i} dersin final notunu giriniz "))
    ortalama=vize*0.4+final*0.6
    if ortalama>=50:
        print("GECTI")
    else:
        print("KALDI")