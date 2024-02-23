
print("quiero mucho demasiado me encanta el ESPATIFILIO!!! mas te vale tener mucho!!!!")

entrada = input("entregar planta: ")

if entrada == "ESPATIFILIO":
    print("siii!!! al fin!!! me gusta!!! el", entrada )
elif entrada == "Espatifilo":
    print("mmm solo eso? bueno tal vez sirva por ahora")
else:
    print("en serio? crees que soy idiota? eso es", entrada)

income = float(input("Introduce el ingreso anual: "))

if income < 85528:
    tax = income * 0.18 - 556.02
else:
    tax = (income - 85528) * 0.32 + 14839.02

tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")