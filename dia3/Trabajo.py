#CONVERTIDOR SOLES/DOLARES
import os
import math
salir ="no"
while(salir=="no"):
    os.system("clear")
    #DATOS DE ENTRADA
    print("===================CONVERTIDOR DE DIVISAS=================")
    
    print ("=========OPCIONES============")
    print("1.Soles a Dolares")
    print("2.Dolares a Soles")
    opcion=int(input("Ingrese la opcion que desea: "))
    
    if opcion==1:
        Monto=int(input("Monto S/: "))
        cambio=int(3)
        
        opcion==1
        operacion="Dolares"
        resultado=Monto//cambio
        
    elif opcion==2:
        Monto= int(input("Cantidad $:"))
        cambio=(3)
        
        opcion==2
        operacion="Soles"
        resultado=Monto*cambio
    else:
        
        print("operacion no valida")
        exit()
        
    if opcion==1:
        print (f"{resultado} USD")
        
    elif opcion==2:
        print (f"{resultado} SOL ")
        
        
    salir=input("Salir? (si/no): ")
    if salir=="si":
        break
        
        
        
        
        
    
    
        
    
    
    
    
