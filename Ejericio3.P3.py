##### ESCRIBE DESDE ACÁ TU CÓDIGO ###### 

def imprime_en_marco(lista):
  tamaño= len(lista)+2
  mayor=0
  for k in lista:
    n= len(k)
    if n>=mayor:
      mayor=n

  for i in range(0,tamaño):
    if i==0 or i==tamaño-1:
      for j in range(0,mayor+4):
        print("#", end='')
      print("")
    
    else:
      
      letras= list(lista[i-1])
      tp= len(letras) 
      dif= mayor-tp
      for h in range(0,tp+4):
        if h==0 or h==tp+3:
          if h==tp+3 and dif!=0:
            for i in range(0,dif):
              print(" ",end='')
          print("#", end='')
        elif h==1 or h==tp+2:
          print(" ", end='')
        else:
          print(letras[h-2], end='')
      print("")

##### ESCRIBE HASTA ACÁ TU CÓDIGO #####

def main():   
  texto = input("Ingresa una frase: ")   
  lista_de_palabras = texto.split(" ")   
  imprime_en_marco(lista_de_palabras) 
 
if __name__ == '__main__':   
  main() 

