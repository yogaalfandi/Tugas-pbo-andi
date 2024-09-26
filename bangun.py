#KUBUS
sisi = float (input("Masukkan sisi kubus: "))
volume = sisi ** 3
luas_permukaan = 6 * (sisi ** 2)
print("Volume kubus: ", volume)
print("Luas permukaan kubus: ", luas_permukaan)

#BALOK
panjang = float(input("Masukkan panjang balok: "))
lebar = float(input("Masukkan lebar balok: "))
tinggi = float(input("Masukkan tinggi balok: "))
volume = panjang * lebar * tinggi
luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
print("Volume balok: ", volume)
print("Luas permukaan balok: ", luas_permukaan)

#TABUNG
jari_jari = float(input("Masukkan jari-jari tabung: "))
tinggi = float(input("Masukkan tinggi tabung: "))
volume = 3.14 * (jari_jari ** 2) * tinggi
luas_permukaan = 2 * 3.14 * jari_jari * (jari_jari + tinggi)
print("Volume tabung: ", volume)
print("Luas permukaan tabung: ", luas_permukaan)

#BOLA
jari_jari = float(input("Masukkan jari-jari bola: "))
volume = (4/3) * 3.14 * (jari_jari **3)
luas_permukaan = 4 * 3.14 * (jari_jari **2)
print("Volume bola: ", volume)
print("Luas permukaan bola: ", luas_permukaan)

#KERUCUT
import math
def kerucut(jari_jari, tinggi):
    s = math.sqrt(jari_jari**2 + tinggi**2)
    volume = (1/3) * math.pi * jari_jari**2 * tinggi
    luas_permukaan = math.pi * jari_jari * (jari_jari + s)
    return volume, luas_permukaan
jari_jari = float(input("Masukkan jari-jari alas kerucut: "))
tinggi = float(input("Masukkan tinggi kerucut: "))
volume, luas_permukaan = kerucut(jari_jari, tinggi)
print(f"Volume kerucut: {volume:.2f}")
print(f"Luas permukaan kerucut: {luas_permukaan:.2f}")

#PRISMA SEGITIGA
import math
def volume_prisma_segitiga(alas, tinggi_segitiga, tinggi_prisma):
    luas_alas = 0.5 * alas * tinggi_segitiga
    volume = luas_alas * tinggi_prisma
    return volume
def luas_permukaan_prisma_segitiga(alas, tinggi_segitiga, sisi_miring, tinggi_prisma):
    luas_alas = 0.5 * alas * tinggi_segitiga
    keliling_alas = alas + tinggi_segitiga + sisi_miring
    luas_permukaan = 2 * luas_alas + keliling_alas * tinggi_prisma
    return luas_permukaan
alas = float(input("Masukkan panjang alas segitiga: "))
tinggi_segitiga = float(input("Masukkan tinggi segitiga: "))
sisi_miring = float(input("Masukkan panjang sisi miring segitiga: "))
tinggi_prisma = float(input("Masukkan tinggi prisma: "))
volume = volume_prisma_segitiga(alas, tinggi_segitiga, tinggi_prisma)
luas_permukaan = luas_permukaan_prisma_segitiga(alas, tinggi_segitiga, sisi_miring, tinggi_prisma)
print(f"Volume prisma segitiga: {volume:.2f} satuan kubik")
print(f"Luas permukaan prisma segitiga: {luas_permukaan:.2f} satuan persegi")