filas = int(input("Introduce el numero de filas: "))
columnas = filas
matriz = []
for i in range(filas):
    matriz.append([])
    for j in range(columnas):
        valor = float(input("fila {}, columna {} : ".format(i+1,j+1)))
        matriz[i].append(valor)

vector = []
vector = input("Introduce el estado inicial del sistema (cada valor separado por un espacio): ")
vector = vector.split(" ")
for i in range(len(vector)):
    vector[i] = int(vector[i])
vector = [vector]
t = int(input("Introduce el numero de clicks del sistema: "))
print(matriz)

m3 = []

for i in range(len(matriz)): 
    m3_fila = []
    for j in range(len(matriz[0])): 
        valor = 0
        for k in range(len(matriz)):
            valor += matriz[i][k] * matriz[k][j]
        m3_fila.append(valor) 
    m3.append(m3_fila) 
   
print(m3)

print(f"{m3} * {vector}")


m4 = []

for i in range(len(m3)): 
    m4_fila = []
    for j in range(len(vector[0])): 
        valor = 0
        for k in range(len(vector)): 
            valor += m3[i][k] * vector[k][j]
        m4_fila.append(valor) 
    m4.append(m4_fila)
print(m4[0])
