"""with open('fotos.txt', 'r') as abrir:
    lista = abrir.read().splitlines()

def remove_repetidos(x):
    l = []
    for i in x:
        if i not in l:
            l.append(i)
    return(l)

outra2 = []
for c in range(len(lista)):
    outra = lista[c].split('_', 1)[0]
    outra2.append(outra)

setada = []
for c in range(0, 19850):
    conta = (f"{outra2[c]} = {outra2.count(outra2[c])}")
    setada.append(conta)

setada = remove_repetidos(setada)
setada = '\n\n'.join(setada)
print(setada)"""


counter_dict = {}
with open('fotos.txt') as f:
	line = f.readline()
	while line:
		line = line[3:-26]
		if line in counter_dict:
			counter_dict[line] += 1
		else:
			counter_dict[line] = 1
		line = f.readline()

print(counter_dict)

