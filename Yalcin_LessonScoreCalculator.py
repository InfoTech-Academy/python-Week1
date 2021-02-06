list = []
ad = (input("Ogrenci adi giriniz:\n"))
soyad = (input("Ogrenci soyadi giriniz:\n"))
no = (input("Ogrenci numarasi giriniz:\n"))
for x in range(1, 5):
    ders = input(str(x) + ". ders adi giriniz:\n")
    list.append(ders)
    vize = (int(input(ders + " dersi icin Vize notu giriniz:\n")))
    final = (int(input(ders + " dersi icin Final notu giriniz:\n")))
    ort = (vize * 0.4) + (final * 0.6)
    if ort >= 50:
        sonuc = "Gecti"
    else:
        sonuc = "Kaldi"
    list.append(sonuc)

print(no, "numarali", ad, soyad)
for x in range(0, 8, 2):
    print(list[x], list[x + 1])