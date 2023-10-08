text_1 = input("Enter the first phrase: ")
text_2 = input("Enter the second phrase: ")
litters_1 = set()
litters_2 = set()

for char in text_1:
    if char.isalpha():
        litters_1.add(char.lower())
for char in text_2:
    if char.isalpha():
        litters_2.add(char.lower())

if litters_2.issubset(litters_1):
    print("Phrase 1:", litters_1)
    print("Phrase 2:", litters_2)
    print("The letters of the first phrase can be used to form the second phrase!")
else:
    print("Phrase 1:", litters_1)
    print("Phrase 2:", litters_2)
    print("The letters of the first phrase can't be used to form the second phrase!")