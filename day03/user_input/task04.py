import re

text = "I love spending time sleeping. Don't you? Sleep more so!"

sentences= re.split(r'[.?!]', text)
#on sépare le texte en phrases après chaque ".?!"
new_sentence=[]
#on stock les phrases créées dans un tableau
for sentence in sentences:
    sentence=sentence.strip()
    # pour chaque phrase on supprime les espaces en début et fin
    if sentence:
        words = sentence.split()
        # on sépare chaque phrase en mot à chaque espace
        if words:
            new_sentence.append(words[0])
            # on stock chaque premier mot dans un tableau

new_text =' '.join(new_sentence)
#on colle chaque mot stocké dans new_sentence en séparant par un espace
print(f"{new_text}.")