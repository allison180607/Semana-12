#Diario personal

from datetime import datetime
ahora = datetime.now()
fecha = ahora.strftime("%Y-%m-%d %H:%M:%S")

entrada=input("Ingrese su entrada para el diario: ")

with open("diario.txt","a",encoding="utf-8") as archivo:
    archivo.write(f"{fecha}\n,{entrada}\n\n")

print("Tu entrada ha sido guardada en el diario") 