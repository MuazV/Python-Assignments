
numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]

most_freq_sayı = max(numbers, key = numbers.count)
frequency = numbers.count(most_freq_sayı)
print(f"The most frequent number is {most_freq_sayı} and it was {frequency} times repeated")

