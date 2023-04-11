array=[]
print("introduzca un numero")
n1 = int(input())
print("introduzca un numero")
n2 = int(input())
print("introduzca un numero")
n3 = int(input())
array.append(n1)
array.append(n2)
array.append(n3)
suma=0
for n in array:
    suma= suma+n
print("La media es "+str(suma/len(array)))