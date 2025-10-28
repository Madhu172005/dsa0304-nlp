import random

text = "the cat sat on the mat"
words = text.split()
bigrams = [(words[i], words[i+1]) for i in range(len(words)-1)]

def generate_bigram_text(start_word, length=5):
    result = [start_word]
    for _ in range(length - 1):
        next_words = [y for x, y in bigrams if x == result[-1]]
        if next_words:
            result.append(random.choice(next_words))
        else:
            break
    return ' '.join(result)

print(generate_bigram_text("the"))
