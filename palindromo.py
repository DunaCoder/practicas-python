import re
def isPalindromo(s):
    minusculas = s.lower()
    patron = r"[^\w\s]"  # Patrón que busca cualquier carácter que no sea alfanumérico o espacio
    palabra = re.sub(patron, "", minusculas)
    invertido = palabra[::-1]
    if palabra == invertido:
        print(f"La palabra '{palabra}' es un palíndromo.")
    else:
        print(f"La palabra '{palabra}' no es un palíndromo.")

entrada = input("ingrese una palabra: ")

isPalindromo(entrada)


