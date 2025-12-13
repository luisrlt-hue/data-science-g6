#Llas tuplas son inmutables

dias=("Lunes","Martes","Miercoles","Jueves","Viernes")
print(f"Tipo de datos orginal:{type(dias)}")
dias=list(dias)
print(f"Tipo de datos modificado:{type(dias)}")
dias.append("Sabado")
dias=tuple(dias)

print(dias)


