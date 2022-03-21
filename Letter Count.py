string = "hippo runs to us!".lower()
dictionary = {}

for i in string:
    letter = string.count(i)
    dictionary[i] = letter

print(dictionary)