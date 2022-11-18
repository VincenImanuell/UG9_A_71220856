skala_fahrenheit = input("Suhu dalam skala Farenheit : ")

cara1 = int(skala_fahrenheit) - 32
cara2 = 1.8
skala_celcius = round(cara1 / cara2) 

print(skala_fahrenheit, " derajat Fahrenheit dikonversi menjadi ", skala_celcius, " derajat Celcius")