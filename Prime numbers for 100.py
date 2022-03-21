list_prime = []

for num in range(2, 100):
        for i in range(2, num):
           if (num % i) == 0:
               break
        else:
            list_prime.append(num)
    
print(list_prime)

# list_prime = []
# element = {}

# for num in range(2,100):
#     for i in range(2,num):
#         if (num%i) == 0:
#             element[str(i)].append(i)
#         else:
#             element[str(i)] = [i]

# print(list(element.values()))

# lst = ["b", "a", "b", "a", "c"]
# elements = {}
# for i in lst:
#     if i not in elements:
#         elements[i] = [i]
#     else:
#         elements[i] += [i]
# print(list(elements.values()))

# list_prime = [num for num in range(2,100) for i in range(2,num) if num%i != 0]
# print(list_prime)

# liste = [5,4,2,5,5,4,3,4,5,2]
# sözlük = {}
# for i in liste :
#   if str(i) in sözlük :
#     sözlük[str(i)].append(i)
#   else:
#     sözlük[str(i)] = [i]
# print(list(sözlük.values()))