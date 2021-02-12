kullanici_adi=input("Ad/Soyadinizi giriniz: ")
ogrenci_numarasi=input("Numaranizi giriniz: ")
count = 0
def ortalama():
    global count
    dersler = list()
    vizeler = list()
    finaller = list()
    ortalama = list()
    sonuc = list()
    while count<=3:
        print(count+1,".Ders icin")
        dersler.append(input("Ders adini giriniz: "))
        vizeler.append(input("Vize notunuzu giriniz"))
        finaller.append(input("Final notunuzu giriniz"))
        ortalama.append(float(vizeler[count])*0.4+float(finaller[count])*0.6)
        if ortalama[count]> 50:
            sonuc.append("GECTI")
        else:
            sonuc.append("KALDI")
        count+=1

    for ders in dersler:

        print (ders, ortalama[dersler.index(ders)], sonuc[dersler.index(ders)])


ortalama()

