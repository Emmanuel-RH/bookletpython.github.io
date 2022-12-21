dolares = input("Ingresa cuántos dolares tienes: ")
dolares = float(dolares)
pesos = 0.051
dolares = dolares / pesos
dolares = round(dolares, 2)
dolares = str(dolares)

nombre_usuario = input("Ingresa tu nombre: ")
nombre_usuario = str(nombre_usuario)
apellido_usuario = input("Ingresa tu apellido: ")
apellido_usuario = str(apellido_usuario)

print("")
print(nombre_usuario + " " + apellido_usuario + ", tienes $" + dolares + " dolares")