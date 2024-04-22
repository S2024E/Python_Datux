# Realice un programa que calcule la suma de los numeros hasta el valor ingresado

msg="""
  1.Desea sumar los numeros
  2.Desea restar los numeros
"""
print(msg)
opcion=int(input("Ingresa una opcion"))
a=int(input("Ingrese un numero"))

if opcion==1:
  print(a+b)
elif opcion==2:
  print(a-b)
else:
  print("Ingrese un valor valido")   
