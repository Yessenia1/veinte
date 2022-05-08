edad: int
promedio: int
beca: int
mensaje: str
edad=int(input("¿cuantos años tienes usted? "))
promedio=int(input("¿cual es su promedio? "))
if edad>18:
    if promedio>=18:
        beca=2000
        mensaje=(f" ") 
    elif promedio>=15:
        beca=1000
        mensaje=(f" ")
    elif promedio<15 and promedio>=12:
        beca=500
        mensaje=(f" ")
    elif promedio<12:
        beca=0
        mensaje=(f"Carta de invitación: invitandolo a que estudie más en el próximo ciclo académico")
elif edad<=18:
    if promedio>=18:
        beca=3000
        mensaje=(f" ")
    elif promedio<18 and promedio>=16:
        beca=2000
    elif promedio<16 and promedio>=12:
        beca=100
        mensaje=(f" ")
    elif promedio<12:
        beca=0
        mensaje=(f"Carta de invitación: invitandolo a que estudie más en el próximo ciclo académico")
print(f"La bonificación de su beca es de {beca} soles {mensaje}")