"""
Beden Kitle Indeksi Hesaplama
Bir kisinin ağırlığının, boyuna göre normal olup olmadığını gösteren parametreye Beden Kitle İndeksi denir.
Kısaca insanın kilosunu kişinin boy uzunluğunun karesine bölersek beden kitle indeksi ortaya çıkar.
Kullanıcıdan kilo ve boy uzunluğunu alip çıkan sonuç 25'in altindaysa NORMAL, 25-30 arasında ise FAZLA KİLOLU,
 30-40 arasında ise OBEZ, 40 ve üzerinde ise AŞIRI ŞİŞMAN şeklinde uyarı yazdiriniz.
"""
print("Beden Kitle İndeksi Hesaplama")
adi = input("İsminiz : ")
soyadi = input("Soyadınız : ")
boyunuz: input("Boyunuz (metre cinsinden) : 1.")
x = "1." + boyunuz
y = float(x)
kilonuz = float(input("Kilonuz : "))
indeks = kilonuz / (y ** 2)
if indeks < 25:
    print("BKİ:", indeks, "Normal")
elif 25 <= indeks <= 30:
    print("BKİ:", indeks, "Fazla Kilolu")
elif 31 <= indeks <= 40:
    print("BKİ:", indeks, "Obez")
else:
    print("BKİ:", indeks, "Asiri Sisman")
