import random
rep=int(input("Ingrese el número de caras a obtener: "))
c=0
s=0
while c!=rep:
  nro=random.randint(1,100)
  if nro%2==0:
    c+=1
  else:
    s+=1
total=s+c
prob= (c/total)*100
print(f"Obtuve {rep} caras de {total} lanzamientos. Eso equivale a {prob}%")

#Tabla(Respuesta en orden)

# 22(45.4545) | 24(41,666%) | 20(50%) | 66(45,7%)
# 203(49,261%) | 197(50,761%) | 209(47.8468%) | 609(49,2896%)
# 1978(50.556%) | 2029(49.285%) | 1997(50,75%) | 6004(50,197%)

#A medida que va aumentando el número, los porcentajes de caras obtenidas se van acercando a 50%