import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')


text = "The quick brown fox jumps over the lazy dog."
tokens = nltk.word_tokenize(text)
tags = nltk.pos_tag(tokens)
print("POS Tags:", tags)
