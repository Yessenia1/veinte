regalo: int
dinero: float
dinero=float(input("¿cuanto dinero tienes para el regalo? "))
if dinero<=10:
    regalo=(f"El regalo sera una tarjeta")
elif dinero>=11 and dinero<=100:
    regalo=(f"El regalo sera un chocolate")
elif dinero>=101 and dinero<=250:
    regalo=(f"El regalo sera flores")
elif dinero>=251:
    regalo=(f"El regalo sera un anillo")
print(f"{regalo} por San Valentin")