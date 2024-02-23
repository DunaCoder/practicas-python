def sumar(n1, n2):
    return n1 + n2

def restar(n1, n2):
    return n1 - n2

def dividir(n1, n2):
    return n1 / n2

def multiplicar(n1, n2):
    return n1 - n2

print("que quieres hacer?")
print("sumar?")
print("restar?")
print("dividir?")
print("o multiplicar?")


orden= input("escribe tu orden aqui: ")

if orden ==  "+":
    n1 = int(input("agrega un numero: "))
    n2 = int(input("agrega un segundo numero: "))
    sumar(n1,n2)
    resultado = n1 + n2
elif orden == "-":
    n1 = int(input("agrega un numero: "))
    n2 = int(input("agrega un segundo numero: "))
    restar(n1,n2)
    resultado = n1 - n2
elif orden == "/":
    n1 = int(input("agrega un numero: "))
    n2 = int(input("agrega un segundo numero: "))
    dividir(n1,n2)
    resultado = n1 / n2
elif orden == "*":
    n1 = int(input("agrega un numero: "))
    n2 = int(input("agrega un segundo numero: "))
    multiplicar(n1,n2)
    resultado = n1 * n2
else:
    print("odern no valida")

print(resultado)