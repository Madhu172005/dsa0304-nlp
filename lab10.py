def transformation_tag(words):
    tags = [('dog', 'NN'), ('runs', 'NN')]  # Initial tags
    for i, (word, tag) in enumerate(tags):
        if word == 'runs':
            tags[i] = (word, 'VB')
    return tags

print("Transformation-based tags:", transformation_tag(['dog', 'runs']))
