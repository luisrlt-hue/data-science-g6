#CALCULADORA

#ENTRADA
numero1=int(input("ingrese el primer numero:"))
numero2=int(input("ingrese el segundo numero"))
operacion=input("ingrese la operacion a realizar (+,-,*,/): ")
 #PROCESO
if operacion == "+":
    resultado=numero1+numero2
elif operacion == "_":
    resultado=numero1-numero2
elif operacion=="x":
    resultado=numero1*numero2
elif operacion=="/":
    resultado=numero1/numero2
else:
    print("operacion no valida")
    exit()

    
#SALIDA
print(f"{numero1}{operacion}{numero2}={resultado}")
            
    
    