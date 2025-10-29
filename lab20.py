from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
docs = [
 "The cat sat on the mat.",
 "The dog barked loudly.",
 "The cat and the dog became friends."
]
query = ["cat and dog"]
vectorizer = TfidfVectorizer()
tfidf = vectorizer.fit_transform(docs + query)
cosine_sim = (tfidf * tfidf.T).toarray()
query_index = len(docs)
scores = cosine_sim[query_index, :-1]
rank = np.argsort(-scores)
print("=== TF-IDF Document Ranking ===")
for i, idx in enumerate(rank):
 print(f"Rank {i+1}: Document {idx+1} (Score = {scores[idx]:.4f}) -> {docs[idx]}")
