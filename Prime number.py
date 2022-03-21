print("###\tWelcome to Find a Prime Number Program\t###")


number = int(input("Please enter a number: "))
sayac = 0
for i in range(2,number):
    if number%i == 0:
        sayac +=1
if sayac != 0:
    print(f" Your number {number} isn't a prime number. It have {sayac+2} dividing")
else:
    print(f"Your number {number} is a prime number.")
        

