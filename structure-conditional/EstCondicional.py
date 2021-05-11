
def ejercicio01():
  #Defenir variables y otros
  print("cuanto se debe pagar el Estacionamiento")
  montoPh=0
  #Datos de entrada
  N=int(input("Ingrese las horas:"))
  #Proceso
  if N<=2:
    montoPh=N*5
  elif N<=5:
    montoPh=((N-2)*4)+10
  elif N<=10:
    montoPh=((N-5)*3)+22
  elif N>10:
    montoPh=((N-10)*2)+37
  #Datos de Salida
  print("Monto a pagar es:",montoPh)
ejercicio01()

def ejercicio02():
  #Defenir variables y otros
  print("personas que pueden botar:")
  #Datos de entrada
  edad=int(input("Ingrese su edad:"))
  #Proceso
  if edad>=18:
   resultado="Puedes botar eres mayor"
  else:
   resultado="No puedes botar eres menor"
  #Datos de Salida
  print("resultado ust.:",resultado)
ejercicio02()

def ejercicio03():
  #Defenir variables y otros
  print("cuanto Pagar al trabajador por hora:")
  PH=0
  #Datos de entrada
  HT=int(input("Ingrese horas trabajadas:"))
  #Proceso
  if HT<=40:
    PH=HT*7.5
  elif HT>40:
    PH=((HT-40)*15)+300
  #Datos de Salida
  print("montoPh:",PH)
ejercicio03()

def ejercicio04():
  #Defenir variables y otros
  print("Que regalo puedes dar segun tu dinero")
  #Datos de entrada
  RG=int(input("Ingrese el dinero:"))
  #Proceso
  if RG<=10:
    resultado="tarjeta"
  elif RG>=11 and RG<101:
    resultado="chocolates"
  elif RG>=101 and RG<251:
    resultado="flores"
  elif RG>=251:
    resultado="anillo"
  #Datos de Salida
  print("resultados:",resultado)
ejercicio04()

def ejercicio05():
  #Defenir variables y otros
  print("buscando el nombre y edad del menor")
  #Datos de entrada
  n1=(input("Ingrese nombre 1:"))
  e1=int(input("Ingrese edad 1:"))
  n2=(input("Ingrese nombre 2:"))
  e2=int(input("Ingrese edad 2:"))
  n3=(input("Ingrese nombre 3:"))
  e3=int(input("Ingrese edad 3:"))
  #Proceso
  if e1<e2 and e1<e3:
    busqueda=n1
    años=e1
  elif e2<e1 and e2<e3:
    busqueda=n2
    años=e2
  elif e3<e1 and e3<e2:
    busqueda=n3
    años=e3
  #Datos de Salida
  print("El nombre del menor es:",busqueda,"y su edad es:",años)
ejercicio05()

def ejercicio06():
  #Defenir variables y otros
  print("costo y descuento del producto")
  pago=0
  #Datos de entrada
  compra=int(input("Ingrese monto de compra:"))
  #Proceso
  if compra>=200:
    pago=(compra-(compra*0.15))
    desucuento=compra*0.15
  elif compra>=100 and compra<200:
    pago=(compra-(compra*0.12)) 
    desucuento=compra*0.12
  elif compra<100:
    pago=(compra-(compra*0.10))
    desucuento=compra*0.10
  #Datos de Salida
  print("El costo del producto es:",pago,"y su desucuento",desucuento)
ejercicio06()
 
def ejercicio07():
  #Defenir variables y otros
  print("saber si ust, califico al bono del gobierno")
  #Datos de entrada
  EN=int(input("Ingrese edad del becado:"))
  PN=int(input("Ingrese promedio:"))
  #Proceso
  if EN>18 and PN>=9:
    paGo=2000
  elif EN>18 and PN>=7.5 and PN<9:
    paGo=1000
  elif EN>18 and PN<7.5 and PN>=6:
    paGo=500
  elif EN>=18 and PN<6:
    paGo="ust.tiene una carta de invitacion para esforzarse el proximo año"   
  elif EN<=18 and PN>=9: 
    paGo=3000
  elif EN<=18 and PN<9 and PN>=8:
    paGo=2000
  elif EN<=18 and PN<8 and PN>=6:
    paGo=100 
  elif EN<=18 and PN<6:
    paGo="ust.tiene una carta de invitacion para esforzarse el proximo año"  
  #Datos de Salida
  print("pago al becado:",paGo) 
ejercicio07()

def ejercicio08():
  #Defenir variables y otros
  print("la tortuga")
  viaje=0
  #Datos de entrada
  km=int(input("Ingrese el costo por km:"))
  preS=int(input("Ingrese el presupuesto:"))
  #Proceso
  if km*1500<=preS:
    viaje="mexico"
  else:
    viaje="quedarse en casa"
  if km*1600<=preS:
    viaje="P.v"
  if km*2400<=preS:
    viaje="Acapulco"
  if km*3600<=preS:
    viaje="cancun"
  #Datos de Salida
  print("ust.puede viajar ah:",viaje)
ejercicio08()

def ejercicio09():
  #Defenir variables y otros
  print("saber cual es mi bono mayor")
  # Datos de entrada
  antiguedad=float(input("Ingrese antiguedad en el trabajo:"))
  salario=float(input("Ingrese salario ganado:"))
  #Proceso
  if antiguedad>2 and antiguedad<5:
    bono1=salario*0.20
  if antiguedad>=5:
    bono1=salario*0.30
  if salario<1000:
    bono2=salario*0.25
  if salario>=1000 and salario<=3500:
    bono2=salario*0.15
  else:
    bono2=salario*0.10 
  if bono1<bono2:
    bonomayor=bono2
  else:
    bonomayor=bono1
  #Datos de Salida
  print("bonificacion por antiguedad:$",bono1)
  print("bonificacion por salario:$",bono2)
  print("bonificacion mayor es de:$",bonomayor)
ejercicio09()

def ejercicio010():
  #Defenir variables y otros
  print("saber cual es mi bono de antiguedad")
  # Datos de entrada
  ant=int(input("Ingrese antiguedad en el trabajo:"))
  #Proceso
  if ant<=5:
    bono=ant*100
  else:
    bono=1000
  #Datos de Salida
  print("bonificacion por antiguedad:$",bono)
ejercicio010()












