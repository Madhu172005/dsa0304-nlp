from nltk.tree import Tree

tree = Tree.fromstring('(S (NP (Det the) (N cat)) (VP (V sees) (NP (Det the) (N dog))))')
tree.pretty_print()
