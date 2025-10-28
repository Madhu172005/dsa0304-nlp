import re

def rule_based_pos_tag(words):
    tagged = []
    for word in words:
        if re.match(r'.*ed$', word):
            tagged.append((word, 'VBD'))
        elif re.match(r'.*ing$', word):
            tagged.append((word, 'VBG'))
        elif re.match(r'.*ly$', word):
            tagged.append((word, 'RB'))
        else:
            tagged.append((word, 'NN'))
    return tagged

words = ["played", "playing", "quickly", "fox"]
tags = rule_based_pos_tag(words)
print("Rule-based POS tags:", tags)
