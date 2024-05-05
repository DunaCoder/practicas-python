lista = [10, 4, 2]
print("Lista original:", lista)

for i in range(len(lista) - 1):  # Recorre hasta el penúltimo elemento
    for j in range(len(lista) - i - 1):  # Recorre el subconjunto restante
        if lista[j] > lista[j + 1]:  # Compara elementos adyacentes
            aux = lista[j]
            lista[j] = lista[j + 1]
            lista[j + 1] = aux

print("Lista ordenada:", lista)
