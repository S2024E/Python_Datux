# Realizar un programa que permita saber si un usuario puede obtener una tarjeta de credito
edad=int(input("Ingrese su edad "))
salario=float(input("Ingrese sus ingreso mensual "))
if edad>18 and salario>1000 and salario<=3000:
    print("Tienes la posibilidad de obtener una tarjeta clasica")
elif edad>18 and salario>3000:
    print("Tienes la posibilidad de obtener una tarjeta dorada")
else:
    print("No cumples con los requisitos minimos")
    restante=18-edad
    print(f"Te faltan {restante} años para adquirir una tarjeta")