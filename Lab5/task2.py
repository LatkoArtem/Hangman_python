scores = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3,
    'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
}
inp = input("Enter words: ")
individual_words = inp.split()

def your_score(word):
    word = word.upper()
    score_list = []
    score_1 = 0 
    for char in word:
        if char in scores:  
            score = scores[char]
            score_list.append(score)
            score_1 += score
    return score_1, score_list
for word in individual_words:
    score_2, score_list = your_score(word)
    print(f"{'+'.join(map(str, score_list))}={score_2}")