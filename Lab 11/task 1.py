import os
file_name_to_find = 'gadsby.txt'
for root, dirs, files in os.walk('/'): 
    if file_name_to_find in files: 
        file_path = os.path.join(root, file_name_to_find)
        print(f'Знайдено файл "{file_name_to_find}" за шляхом: {file_path}')
        break
with open(file_path, 'r') as file:
    text = file.read().lower()
letter_counts = {}
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for char in alphabet:
    value = 0
    for letter in text:
        if letter.isalpha() and char == letter:
            value += 1
    letter_counts[char] = value

total_letters = sum(letter_counts.values())
sorted_letter_counts = sorted(letter_counts.items(), key=lambda item: item[1], reverse=True)
percentage_taste = 0
for char, value in sorted_letter_counts:
    letter_percentage = (value / total_letters) * 100
    percentage_taste += letter_percentage
print("TOP 5 by percentage:")
for char, value in sorted_letter_counts[:5]:
    letter_percentage = (value / total_letters) * 100
    print(f"{char}: {value} ({letter_percentage:.3f}%)")
print("\n5 LAST by percentage")
for char, value in sorted_letter_counts[-5:]:
    letter_percentage = (value / total_letters) * 100
    print(f"{char}: {value} ({letter_percentage:.3f}%)")