print("***Uzaklık Birimlerini Dönüştürme Programına Hoşgeldiniz***", end="\n\n")

uzaklık_km = float(input("Lütfen Dönüştürmek İstediğiniz Uzaklık Birimini Kilometre Cinsinden Giriniz: "))
uzaklık_miles = uzaklık_km * 0.62
sonuc = f"{uzaklık_km} kilometre, {uzaklık_miles} mile eşittir."
print(sonuc)