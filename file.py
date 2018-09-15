import math
import pprint

vals = [3, 4, 5, 6, 7, 9, 2, 3, 4, 5, 7, 9, 1, 3, 4, 6, 8]

#element = input()
#while True:
#    if element != ' ' and element == '123456789':
#        vals.append(element)
#        print(vals)
#    else:
#        break
#print(vals)

def mean(vals):
    if len(vals) > 0:
        return float(sum(vals))/len(vals)
    else:
        return 'Not available'

    

print(mean(vals))

vowels = 'eyuioa'
consonants = 'ptk'
for v in vowels:
    for c in consonants:
        print(c + v)

nouns = 'derevo vnizu'
verbs = 'stoyalo bilo lezhalo'
for S in nouns.split():
    for V in verbs.split():
        for O in nouns.split():
            print(S + ' ' + V + ' ' + O)

#sentence1 = 'THEY LIKE VEGETABLES AND FRUITS'
#sentence2 = 'LIKE'
#sentence3 = 'VEGETABLES'
#sentence4 = 'AND'
#sentence5 = 'FRUITS'
#def glasni:
#    for letter 
