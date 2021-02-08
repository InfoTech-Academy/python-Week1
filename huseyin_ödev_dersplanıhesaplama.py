#Ders Puani Hesaplama
#Kullanıcıdan Adi, Soyadi, Ogrenci Numarasi, 4 ders adi, bu derslerin Vize ve Final notlari istenecektir. 
#Vize notunun % 40′ı ile Final Notunun %60′ınin toplamı yil sonu ortalamasini verecektir. 
#Ortalama 50‘den küçükse ekranda “KALDI“, 50 ve üstüyse ekranda “GEÇTİ” yazdırılacaktır.
#Bu yazdirma islemi 4 ders icinde yapilacak ve dersler alt alta yazdirilacaktir.



kullanıcı_adı       =input("Lütfen Kullanıcı Adınızı Giriniz: ")
kullanıcı_soyadı    =input("Lütfen Kullanıcı Soyadınız Giriniz: ")
öğrenci_numarası    =int(input("Lütfen Öğrenci Numaranızı Giriniz: "))

ders=[]
ort=[]

i=0
while (i<4):
    ders_adı            =input("Lütfen Ders Adını Giriniz: ")
    ders.append(ders_adı)
    vize_notu           =int(input("Vize Notunuzu Giriniz: "))
    final_notu          =int(input("Lütfen Final Notunuzu Giriniz: "))
    ortalama           =float(vize_notu*0.40+final_notu*0.60)
    ort.append(ortalama)
    i+=1

i=0
while(i<4):
    if ort[i]<50:
        print("{} {} {} {} {} KALDI".format(kullanıcı_adı,kullanıcı_soyadı,öğrenci_numarası,ders[i],ort[i]))
        i+=1 
    
    else:
        print("{} {} {} {} {} GEÇTİ".format(kullanıcı_adı,kullanıcı_soyadı,öğrenci_numarası,ders[i],ort[i])) 

    
    
   