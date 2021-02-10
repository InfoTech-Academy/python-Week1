'''
3- Beden Kitle Indeksi Hesaplama
Bir kisinin ağırlığının, boyuna göre normal olup olmadığını gösteren parametreye Beden Kitle İndeksi denir. 
Kısaca insanın kilosunu kişinin boy uzunluğunun karesine bölersek beden kitle indeksi ortaya çıkar. 
Kullanıcıdan kilo ve boy uzunluğunu alip çıkan sonuç
 25'in altindaysa NORMAL, 25-30 arasında ise FAZLA KİLOLU, 30-40 arasında ise OBEZ, 40 ve üzerinde ise AŞIRI ŞİŞMAN şeklinde uyarı yazdiriniz.
 '''
 # kilo / boy ** 2 
'''
def bmi (kilo,boy):
    vke = int(kilo) / (float(boy)**2)
    print(f"Beden kitle indeksi: {round(vke)}")
    if vke < 25:
        print("normal")
    elif vke >= 25 and vke < 30:
        print("fazla kilolu")
    elif vke >= 30 and vke < 40:
        print("obez")
    else:
        print("aşırı şişman")
    

kilo =input("kişinin kilosunu giriniz: ")
boy = input("kişinin boyunu metre cinsinden giriniz (1.75 gibi): ")

bmi(kilo,boy)
'''
# veya

kilo =input("kişinin kilosunu giriniz: ")
boy = input("kişinin boyunu metre cinsinden giriniz (1.75 gibi): ")
vke = int(kilo) / (float(boy)**2)
print(f"Beden kitle indeksi: {round(vke)}")
if vke < 25:
    print("normal")
elif vke >= 25 and vke < 30:
    print("fazla kilolu")
elif vke >= 30 and vke < 40:
    print("obez")
else:
    print("aşırı şişman")