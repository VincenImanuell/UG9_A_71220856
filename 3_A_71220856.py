panjang = input("Masukkan panjang : ")
lebar = input("Masukkan lebar : ")
jari = input("Masukkan jari-jari : ")

luas_persegipanjang = int(panjang)*int(lebar)
luas_lingkaran = (int(jari)*int(jari))*3.14*0.5
luas_total = luas_persegipanjang + luas_lingkaran
kaleng = round(luas_total / 15)

print("Area tersebut membutuhkan", kaleng, " kaleng cat")