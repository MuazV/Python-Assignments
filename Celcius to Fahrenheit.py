print("***Sıcaklık Derecelerini Dönüştürme Programına Hoşgeldiniz***", end="\n\n")

sıcaklık_celc = float(input("Lütfen Dönüştürmek İstediğiniz Sıcaklık Derecesini Celsius Olarak Giriniz:"))
sıcaklık_fahr = sıcaklık_celc * 1.8 + 32
sonuc = f"{sıcaklık_celc} derece Celcius sıcaklık, {sıcaklık_fahr} derece Fahrenheit sıcaklığa eşittir."
print(sonuc)