word = input("Enter you Word: ")
vowels = "aeiouAEIOU"
count = 0
found_vowels = []
for letter in word:
    if letter in vowels:
        count += 1
        found_vowels.append(letter)
print("Total vowels found: ", count)
print("Vowels found: ", found_vowels)
print("Unique vowels:", set(found_vowels))



