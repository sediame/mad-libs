import re

with open('data/template.txt') as f:
    mylist = list(f)

text = mylist[0]
print('Enter an adjective:')
new1 = input()

print('Enter a noun:')
new2 = input()

print('Enter a verb:')
new3 = input()

print('Enter a noun:')
new4 = input()

text = re.sub("ADJECTIVE", new1, text, count=1)

text = re.sub("NOUN", new2, text, count=1)

text = re.sub("VERB", new3, text, count=1)

text = re.sub("NOUN", new4, text, count=1)
print(text)
f.close()

ff = open('data/result.txt', 'w')
ff.write('%s' % text)
ff.close()
