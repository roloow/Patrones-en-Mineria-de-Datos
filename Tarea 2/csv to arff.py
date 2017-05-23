
f = open("groceries.csv")

#lectura de productos diferentes
linea = f.readline()
my_set = set([])
while linea != '' :
	elementos = linea.split(",")
	for elemento in elementos :
		elemento = elemento.split("\n")
		my_set.add(elemento[0])
	linea = f.readline()

f.close()
my_set = list(my_set)
f = open("groceries.csv")
matriz = []
for linea in f:
	linea = linea.strip().split(',')
	vector = []
	for i in my_set:
		if i in linea:
			vector.append('1')
		else:
			vector.append('0')
	matriz.append(vector)

f.close()
f = open("matriz.csv","w")
f.write(','.join(my_set)+ '\n')
for i in matriz :
	f.write(','.join(i)+'\n')

