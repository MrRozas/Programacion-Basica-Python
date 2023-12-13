import arrow

print("Escribe una fecha de reunión. Sigue el formato YYYY-MM-DD HH:mm:ss ZZZ. Por ejemplo: 2020-07-13 18:00:00 America/Santiago")
datos=input("Ingrese fecha: ")
fecha= arrow.get(datos, 'YYYY-MM-DD HH:mm:ss ZZZ')
rep= int(input("¿A cuántas zonas horarias lo deseas transformar? "))
for i in range(0,rep):
  zona= input("Ingrese la zona horaria de destino: ")
  print(fecha.to(zona))
