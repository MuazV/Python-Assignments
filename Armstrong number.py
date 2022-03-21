# print("###\t Yazdığınız Sayı Armstrong Bir Sayı mı Değil mi Gelin Beraber Bakalım \t###" "\n \t\t\t\t Hoşgeldiniz")

# while True:
#     arms = input("Lütfen Bir sayı Giriniz:")
#     if arms.isnumeric():
#         sayı = list(arms)
#         toplam = 0
#         for i in sayı:
#             y = int(i)**(len(sayı))
#             toplam += y
#         if int(arms) == toplam:
#             print(f"{arms} sayısı bir Armstrong sayıdır.")
#             break
#         else:
#             print(f"Yazdığınız {arms} sayısı Armstrong kriterlerine uymamaktadır.")
#             break
#     else:
#         print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
        

while True :
    
    number = input("Enter a positive integer number :")
    digits = len(number)
    summ = 0
    
    if not number.isdigit() :
        
        print(number, " is invalid entry. Please enter valid input.")
        
    elif int(number) >= 0 :
        
        for i in range(digits) :
            
            summ = summ + int(number[i]) ** digits
            
        if summ == int(number) :
            print(number, " is an Armstrong Number.")
            break
        else :
            print(number, " is not an Armstrong Number.")
            break

