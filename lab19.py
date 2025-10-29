from nltk.wsd import lesk
from nltk.corpus import wordnet
sentence = "He went to the bank to deposit his money"
word = "bank"
sense = lesk(sentence.split(), word)
print("=== Lesk Algorithm ===")
print("Sentence:", sentence)
print("Best Sense:", sense)
print("Definition:", sense.definition())
