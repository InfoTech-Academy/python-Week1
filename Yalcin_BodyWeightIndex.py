# Beden Kitle Indeksi Hesaplama
# Bir kisinin ağırlığının, boyuna göre normal olup olmadığını gösteren parametreye Beden Kitle İndeksi denir.
# Kısaca insanın kilosunu kişinin boy uzunluğunun karesine bölersek beden kitle indeksi ortaya çıkar.
# Kullanıcıdan kilo ve boy uzunluğunu alip çıkan sonuç 25'in altindaysa NORMAL, 25-30 arasında ise FAZLA KİLOLU, ' \
# 30-40 arasında ise OBEZ, 40 ve üzerinde ise AŞIRI ŞİŞMAN şeklinde uyarı yazdiriniz.

weight = int(input("Enter your weight in kilograms: "))
height = int(input("Enter your height in centimeters: "))

index = weight / (height ** 2)

if index < 25:
    print("NORMAL")
elif index < 30:
    print("OVERWEIGHT")
elif index < 40:
    print("OBESE")
else:
    print("EXTREMELY OBESE")
