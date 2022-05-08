c: int
seguro: int
alcohol: int
lentes: int
enfermedad: int
edad: int
cargo1: int
cargo2: int
cargo3: int 
cargo4: int 
seguro=int(input("elija un seguro a=1/b=2 : "))
alcohol=int(input("¿usted tiene el habito de beber alcohol? si=1/no=2 : "))
lentes=int(input("¿usted usa lentes? si=1/no=2 : "))
enfermedad=int(input("¿usted tiene alguna enfermedad? si=1/no=2 : "))
edad=int(input("¿cuantos años tiene? "))
if seguro<=1:
    c=1200
    if alcohol<=1:
        cargo1=c+(c*0.10)
    elif alcohol>=2:
        cargo1=c
    if lentes<=1:
        cargo2=cargo1+(c*0.5)
    elif lentes>=2:
        cargo2=cargo1
    if enfermedad<=1:
        cargo3=cargo2+(c*0.5)
    elif enfermedad>=2:
        cargo3=cargo2
    if edad>40:
        cargo4=cargo3+(c*0.20)
    elif edad<=40:
        cargo4=cargo3+(c*0.10)

elif seguro>=2:
    c=950
    if alcohol<=1:
        cargo1=c+(c*0.10)
    elif alcohol>=2:
        cargo1=c
    if lentes<=1:
        cargo2=cargo1+(c*0.5)
    elif lentes>=2:
        cargo2=cargo1
    if enfermedad<=1:
        cargo3=cargo2+(c*0.5)
    elif enfermedad>=2:
        cargo3=cargo2
    if edad>40:
        cargo4=cargo3+(c*0.20)
    elif edad<=40:
        cargo4=cargo3+(c*0.10)

print(f"El costo de la poliza es {cargo4}")