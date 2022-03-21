
word = input("Lütfen bir kelime giriniz:")
word_list = set(word)

right = {'y', 'u', 'i', 'o', 'p', 'h', 'j','k', 'l', 'n', 'm'}
left = {'q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b'}

if (word_list & left) and (word_list & right):
    print("This is comfortable words")
else:
    print("This is not comfortable words")

    

