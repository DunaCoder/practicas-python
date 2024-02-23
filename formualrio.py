print("bienvenido, por favor ingrese sus datos")
intentos = 1

while intentos <= 3:
    usuario = input("usuario: ")
    contraseña = input("contraseña: ")
    if usuario == "jenny" and contraseña == "gatos333":
        print("bienvenida señorita ", usuario)
        break
    else:
        print("contraseña o usuarios incorrectos")
        intentos += 1
        #print(f"Te quedan {intentos_restantes} intentos.")

if intentos > 3:
    print("demasiados intentos, bloqueando sistema")
