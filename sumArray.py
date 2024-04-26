def sum_array(a):
  
    if not a:
        return 0
    else:
        total = 0
    for n in a:
        total += n
    return total


resultado = sum_array([1, 5.2, 4, 0, -1])
print(resultado)

# def sum_array(lista_numeros):
#   """
#   Esta función toma una matriz de números y devuelve la suma de los números.
#   La función puede manejar números negativos y no enteros.
#   Si la matriz está vacía, devuelve 0.
#   """
#   if not lista_numeros:
#     return 0
#   else:
#     suma = 0
#     for numero in lista_numeros:
#       suma += numero
#     return suma

# # Ejemplo de uso
# resultado = sum_array([1, 5.2, 4, 0, -1])
# print(resultado)  # Salida: 9.2

# resultado = sum_array([])
# print(resultado)  # Salida: 0

# resultado = sum_array([-2.398])
# print(resultado)  # Salida: -2.398
