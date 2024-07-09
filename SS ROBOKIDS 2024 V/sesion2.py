#Actividad "mi primer hello world"
print("Hello, World!")


#ejemplo para el if elif else
nota=int(input("¿cual es tu calificacion? "))

if nota >= 90:
    print("Tienes una A.")
elif nota >= 80:
    print("Tienes una B.")
elif nota >= 70:
    print("Tienes una C.")
elif nota >= 60:
    print("Tienes una D.")
else:
    print("Tienes una F.")


#Ejemplo del while y el for

#Contar del 1 al 5 con While:
contador = 1
while contador <= 5:
    print("El contador es:", contador)
    contador += 1

#Contar del 1 al 5 con For:
for i in range(1,6):
    print("El valor de i es:", i)
