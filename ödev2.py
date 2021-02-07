"""
Kullanıcıdan Adi, Soyadi, Ogrenci Numarasi, 4 ders adi, bu derslerin Vize ve Final notlari istenecektir.
 Vize notunun % 40′ı ile Final Notunun %60′ınin toplamı yil sonu ortalamasini verecektir.
 Ortalama 50‘den küçükse ekranda “KALDI“, 50 ve üstüyse ekranda “GEÇTİ” yazdırılacaktır.
 Bu yazdirma islemi 4 ders icinde yapilacak ve dersler alt alta yazdirilacaktir.
"""
ogrenci_ad = input("Öğrencinin Adı : ")
ogrenci_soyad = input("Öğrencinin Soyadı : ")
ogrenci_no = input("Öğrencinin Numarası : ")
ders1 = input("1.Ders : ")
while True:
    vize1 = int(input("Vize Notunuz : "))
    final1 = int(input("Final Notunuz : "))
    if (0 <= vize1) and (vize1 <= 100) and (0 <= final1) and (final1 <= 100):
        break
    else:
        print(ders1, "Dersi İçin Lütfen 0-100 Arasında Sayısal Değer Giriniz")
        continue
ortalama1 = (vize1 * 0.4) + (final1 * 0.6)
ders2 = input("2.Ders : ")
while True:
    vize2 = int(input("Vize Notunuz : "))
    final2 = int(input("Final Notunuz : "))
    if (0 <= vize2) and (vize2 <= 100) and (0 <= final2) and (final2 <= 100):
        break
    else:
        print(ders2, "Dersi İçin Lütfen 0-100 Arasında Sayısal Değer Giriniz")
        continue
ortalama2 = (vize2 * 0.4) + (final2 * 0.6)
ders3 = input("3.Ders : ")
while True:
    vize3 = int(input("Vize Notunuz : "))
    final3 = int(input("Final Notunuz : "))
    if (0 <= vize3) and (vize3 <= 100) and (0 <= final3) and (final3 <= 100):
        break
    else:
        print(ders3, "Dersi İçin Lütfen 0-100 Arasında Sayısal Değer Giriniz")
        continue
ortalama3 = (vize3 * 0.4) + (final3 * 0.6)
ders4 = input("4.Ders : ")
while True:
    vize4 = int(input("Vize Notunuz : "))
    final4 = int(input("Final Notunuz : "))
    if (0 <= vize4) and (vize4 <= 100) and (0 <= final4) and (final4 <= 100):
        break
    else:
        print(ders4, "Dersi İçin Lütfen 0-100 Arasında Sayısal Değer Giriniz")
        continue
ortalama4 = (vize4 * 0.4) + (final4 * 0.6)
ortalamalar = [ortalama1, ortalama2, ortalama3, ortalama4]
dersler = [ders1, ders2, ders3, ders4]
print(ogrenci_no, "Numaralı Sayın", ogrenci_ad, ogrenci_soyad, "Notlarınız Aşağıda Belirtilmiştir.")
for i in dersler:
    if i == dersler[0]:
        if ortalama1 < 50:
            print(i, "Dersi Ortalamanız : ", ortalama1, "Kaldınız")
        else:
            print(i, "Dersi Ortalamanız : ", ortalama1, "Geçtiniz")
    elif i == dersler[1]:
        if ortalama2 < 50:
            print(i, "Dersi Ortalamanız : ", ortalama2, "Kaldınız")
        else:
            print(i, "Dersi Ortalamanız : ", ortalama2, "Geçtiniz")
    elif i == dersler[2]:
        if ortalama3 < 50:
            print(i, "Dersi Ortalamanız : ", ortalama3, "Kaldınız")
        else:
            print(i, "Dersi Ortalamanız : ", ortalama3, "Geçtiniz")
    else:
        if ortalama4 < 50:
            print(i, "Dersi Ortalamanız : ", ortalama4, "Kaldınız")
        else:
            print(i, "Dersi Ortalamanız : ", ortalama4, "Geçtiniz")
