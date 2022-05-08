edad:int
mensaje:str
edad=int(input("Ingrese su edad:"))
if edad>=18:
  mensaje=(f"Usted puede votar porque su edad es {edad}")
else:
  mensaje=(f"Usted no puede votar porque su edad es {edad}")
print(f"{mensaje}")