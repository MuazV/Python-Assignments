# Define a function named my_fact to calculate factorial of the given number. Given a non-negative integer return the factorial of the integer.

# (Example: The factorial of 5 is: 5*4*3*2*1 = 120 and factorial of 0 is: 1)
# For example:

# Test	Result
# print(my_fact(5))
# 120
# print(my_fact(4))
# 24
# print(my_fact(3))
# 6

def my_fact(n) :
    
    sonuc = 1
    
    for i in range(1, n+1) :
        sonuc *= i
        
    if n == 0 or n == 1 :
        return 1
    else :
        return sonuc


print(my_fact(3))
