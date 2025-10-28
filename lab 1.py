import re

text = "The rain in Spain falls mainly in the plain."
pattern = r"in \w+"

matches = re.findall(pattern, text)
print("Matches:", matches)

search_result = re.search(r"Spain", text)
if search_result:
    print("Found 'Spain' at:", search_result.start())
