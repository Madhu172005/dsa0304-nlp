import spacy
nlp = spacy.load("en_core_web_sm")
text = "Apple Inc. was founded by Steve Jobs in California in 1976."
doc = nlp(text)
print("=== Named Entity Recognition (NER) ===")
for ent in doc.ents:
 print(f"{ent.text:<20} -> {ent.label_}")
