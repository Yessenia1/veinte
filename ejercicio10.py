cobrokm: int
pasaje: int
destinos: int
cobrokm=int(input("¿cuanto cobra por kilometro? "))
destino=int(input("Elija los destinos de viaje son: Tacna=1, Lima=2, Chiclayo=3, Tumbes=4, ninguno=5 : "))
if destino<=1:
    pasaje=(cobrokm*750)*2
    mensaje=(f"El pasaje para Tacna es de {pasaje} soles")
elif destino>=2:
    pasaje=(cobrokm*800)*2
    mensaje=(f"El pasaje para Lima es de {pasaje} soles")
elif destino>=3:
    pasaje=(cobrokm*1200)*2
    mensaje=(f"El pasaje para Chiclayo es de {pasaje} soles")
elif destino>=4:
    pasaje=(cobrokm*1800)*2
    mensaje=(f"El pasaje para Tumbes es de {pasaje} soles")
elif destino>=5:
    pasaje=0
    mensaje=(f"Usted no hizo la compra del pasaje")
print(f"{mensaje}")