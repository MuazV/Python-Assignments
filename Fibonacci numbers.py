
son_sayı = int(input("Write the last Fibonacci number you want to see in the list: "))
Fibo_numbers = []
a = 0
b = 1
for i in range(1,100):
    Fibo_numbers.append(b)
    a , b = b, a + b
    if b > son_sayı:
        break
    
print(f"Fibonacci numbers you want to list = {Fibo_numbers}")