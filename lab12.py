from nltk.parse import EarleyChartParser

grammar = CFG.fromstring("""
  S -> NP VP
  NP -> Det N | Name
  VP -> V NP | V
  Det -> 'the' | 'a'
  N -> 'cat' | 'dog' | 'dogs'
  Name -> 'John' | 'Mary'
  V -> 'sees' | 'see' | 'barks' | 'eats'
""")
parser = EarleyChartParser(grammar)
sentence = "the cat sees the dog".split()

for tree in parser.parse(sentence):
    print(tree)
