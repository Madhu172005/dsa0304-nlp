from nltk.corpus import wordnet as wn
word = "bank"
print("=== WordNet Synsets for 'bank' ===")
for syn in wn.synsets(word):
 print(f"Synset: {syn.name()}")
 print("Definition:", syn.definition())
 print("Examples:", syn.examples())
 print("-" * 40)
