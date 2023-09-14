sentence = 'This is a test. Is it possible to fly? Good things come to those who never give up. '
newSentence = ''

for i in range(0, len(sentence)):
    if(i == 0):
        while sentence[i] != ' ':
            newSentence += sentence[i]
            i += 1
    if((sentence[i] == '.') or (sentence[i] == '?') and (i < len(sentence) -2)):
        print(sentence[i])
        i += 2
        newSentence += ' '
        while sentence[i] != ' ':
            newSentence += sentence[i]
            i += 1

print(newSentence)