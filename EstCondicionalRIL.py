

def ejercicio01RSIL():
  #Defenir variables y otros
  print("1: notas del alumno RSIL:")
  promedio=0
  #Datos de entrada
  NotasRSIL1=float(input("Ingrese nota de primera unidad:"))
  NotasRSIL2=float(input("Ingrese nota de segunda unidad:"))
  NotasRSIL3=float(input("Ingrese nota de tercera unidad:"))
  NotasRSIL4=float(input("Ingrese nota de cuarta unidad:")) 
  #Proceso
  if NotasRSIL1 and NotasRSIL2 and NotasRSIL3 and NotasRSIL4:
    promedio=(NotasRSIL1*0.20)+(NotasRSIL2*0.15)+(NotasRSIL3*0.15)+(NotasRSIL4*0.50)
  #Datos de Salida
  print(".....Tu Nota final del curso de programacion es:",promedio)
ejercicio01RSIL()




def ejercicio02RSIL():
  #Defenir variables y otros
  print("2: Bono por desempeño de maestros RSIL:")
  #Datos de entrada
  puntosRSIL=float(input("Ingrese puntos:"))
  #Proceso
  if puntosRSIL>50 and puntosRSIL<=100:
    bonoRSIL=930*0.10
  elif puntosRSIL>=101 and puntosRSIL<=150:
    bonoRSIL=930*0.40
  elif puntosRSIL>151: 
    bonoRSIL=930*0.70
  else:
    bonoRSIL="error puntos insuficientes vuelva a intentarlo en otra ocacion"
  #Datos de Salida
  print(".....Tu bono por desempeño es:",bonoRSIL,"y tus puntos son:",puntosRSIL)
ejercicio02RSIL()




def ejercicio03RSIL():
  #Defenir variables y otros
  print(" 3: Algoritmo para la aplicacion de la vacuna contra el covid RSIL :")
  #Datos de entrada
  edadRSIL=int(input("Ingrese edad:"))
  sexoRSIL=int(input("Ingrese su sexo \n1=Mujer \n2=Varon \n:"))
  #Proceso
  if edadRSIL>70:
    TIPOdeBACUNA="C"
  elif edadRSIL>=16 and edadRSIL<=69 and sexoRSIL==1:
    TIPOdeBACUNA="C"
  elif edadRSIL>=16 and edadRSIL<=69 and sexoRSIL==2:
    TIPOdeBACUNA="A"
  else:
    TIPOdeBACUNA="A"  
  #Datos de Salida
  print(".....El tipo de bacuna que te corresponde es:",TIPOdeBACUNA)
ejercicio03RSIL()





def ejercicio04RSIL():
  #Defenir variables y otros
  print("4: Calculando operaciones aritmeticas con RSIL:")
  resultado=0
  #Datos de entrada
  operador=(input("Ingrese operador matematico:"))
  valor1=float(input("Ingrese valor 1:"))
  valor2=float(input("Ingrese valor 2:"))
  #Proceso
  if operador=='+':
   resultado=valor1+valor2
  if operador=='-':
   resultado=valor1-valor2
  if operador=='*':
   resultado=valor1*valor2
  if operador=='/':
   resultado=valor1/valor2
  if operador=='^':
   resultado=valor1^valor2
  #Datos de Salida
  print("....El resultado de su operacion es:",resultado)
ejercicio04RSIL()






def ejerciciomultiple05RSIL():
  #Defenir variables y otros
  print("5: Calculando operaciones aritmeticas con RSIL:")
  #Datos de entrada
  operador=int(input("Ingrese operador matematico\n1=resta\n2=suma\n3=multiplicacion\n4=division\n:"))
  valor1=float(input("Ingrese valor 1:"))
  valor2=float(input("Ingrese valor 2:"))
  #Proceso
  if operador==1:
    resultado=valor1-valor2
    operador="suma"
  elif operador==2:
    resultado=valor1+valor2
    operador="resta"
  elif operador==3:
    resultado=valor1*valor2
    operador="multiplicacion"
  elif operador==4:
    resultado=valor1/valor2
    operador="division"
  else:
    print("La opcion que ingreso no existe! intente nuevamente....")
  #Datos de Salida
  print("....El resultado de su:",operador,"es:",resultado)
ejerciciomultiple05RSIL()






  





















