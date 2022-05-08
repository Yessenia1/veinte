horas: float
precio: float
horas=float(input("¿cuntas horas uso el estacionamiento? "))
if horas<=2:
    precio=horas*5
elif horas<=5:
    precio=horas*4
elif horas<=10:
    precio=horas*3
elif horas>=10:
    precio=horas*2
print(f"El precio por las horas en el estacionamiento es de: {precio} soles")