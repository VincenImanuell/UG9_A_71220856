print("===================CAFE===================\n=========MASUKKAN JUMLAH PESANAN==========")

cappucino = input("CAPPUCINO\tDISKON 50%\tRp 25.000\t:")
vanilla_latte = input("VANILLA LATTE\tDISKON 65%\tRp 22.000\t:")
americano = input("AMERICANO\tDISKON 35%\tRp 30.000\t:")
brewed_coffee = input("BREWED COFFEE\tDISKON 40%\tRp 20.000\t:")

harga_cappucino = int(cappucino)*(25000-(25000*(50/100)))
harga_vanilla = int(vanilla_latte)*(22000-(22000*(65/100)))
harga_americano = int(americano)*(30000-(30000*(35/100)))
harga_brewed = int(brewed_coffee)*(20000-(20000*(40/100)))

print("===============TOTAL===============\nTOTAL CAPPUCINO\t\t: Rp",harga_cappucino)
print("TOTAL VANILLA LATTE\t: Rp",harga_vanilla)
print("TOTAL AMERICANO\t\t: Rp",harga_americano)
print("TOTAL BREWED COFFEE\t: Rp",harga_brewed)

total = harga_cappucino + harga_vanilla + harga_americano + harga_brewed

print("Jumlah total biaya yang harus dibayar adalah Rp ", total)