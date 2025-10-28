from nltk.stem import PorterStemmer

words = ["running", "flies", "bigger", "easily"]
stemmer = PorterStemmer()
stems = [stemmer.stem(word) for word in words]
print("Stems:", stems)
