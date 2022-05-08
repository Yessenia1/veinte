costo: float
decuento: float
porcentaje: int
costo=float(input("¿cual es el precio del articulo?"))
if costo>=200:
    descuento=costo-(costo*0.15)
    porcentaje=15
elif costo>100 and costo<200:
    descuento=costo-(costo*0.12)
    porcentaje=12
elif costo<100:
    descuento=costo-(costo*0.10)
    porcentaje=10
print(f"El precio del articulo con descuento es {descuento} y es descuento es de {porcentaje}%")