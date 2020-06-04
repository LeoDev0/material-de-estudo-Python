import string

with open('texto.txt', 'r') as f:
	text = (f.read())
	
text = text.lower()
for c in string.punctuation:
    text = text.replace(c, ' ')
text = text.split()

dic = dict()
for c in text:
    if c not in dic:
        dic[c] = 1
    else:
        dic[c] += 1

for k, v in dic.items():
    print('A palavra "{}" apareceu {} vezes'.format(k, v))
