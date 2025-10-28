words = ['run', 'quick', 'fox', 'over']
tag_dict = {'run': 'VB', 'quick': 'JJ', 'fox': 'NN', 'over': 'IN'}

tags = [(word, tag_dict.get(word, 'NN')) for word in words]
print("Simple POS tags:", tags)
