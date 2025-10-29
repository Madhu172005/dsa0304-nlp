from nltk import PCFG, ChartParser

grammar = PCFG.fromstring("""
  S -> NP VP [1.0]
  NP -> Det N [0.4] | Name [0.6]
  VP -> V NP [0.7] | V [0.3]
  Det -> 'the' [0.6] | 'a' [0.4]
  N -> 'cat' [0.5] | 'dog' [0.5]
  Name -> 'John' [0.5] | 'Mary' [0.5]
  V -> 'sees' [0.5] | 'barks' [0.5]
""")
parser = ChartParser(grammar)
sentence = "the cat sees the dog".split()

for tree in parser.parse(sentence):
    print(tree)
