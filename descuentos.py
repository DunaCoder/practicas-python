#no inluye ningu impuesto
while True:
    producto = input("Ingrese el nombre del producto: ")
    if producto:  # Verificamos que el producto no esté vacío
        break  # Si no está vacío, salimos del bucle
    else:
        print("Error: El nombre del producto no puede estar vacío.")


while True:
    try:
        valor = float(input(f"Ingrese valor del {producto}: "))
        if valor >= 0:
            break
        else:
            print("Error: El valor del producto no puede ser negativo.")
    except ValueError:
        print("Error: El valor ingresado no es un número válido.")

while True:
    try:
        cantidad = int(input(f"Ingrese cantidad de {producto}: "))
        if cantidad > 0:
            break
        else:
            print("Error: La cantidad del producto no puede ser 0 o negativa.")
    except ValueError:
        print("Error: El valor ingresado no es un número entero válido.")

precio = valor * cantidad

if precio >= 350.00:
    descuento = precio * 0.50
    total = precio - descuento
    print(f"El total a pagar con el descuento es de: {total:.2f}$")
else:
    total = precio
    print(f"El total a pagar es de: {total:.2f}$")

print("Tenga buen día :)")
