#Karen Jocelyn Hernández Romero
#Suma de un arreglo
#Teniendo un arreglo de enteros encuentra el resultado de la suma de los elementos del arreglo.
#Reglas:
#ar[i] <= 1000 (El arreglo debe de ser menor a mil datos)
#Tienes que crear la función que haga la suma


arr=[]
def  suma(arr):
    sumar=0
    for i in arr:
        sumar=sum(arr)
        return sumar


tamaño= int(input('Escribe un numero entre el 1 y el 1000: '))

if tamaño <=1000:
 for i in range(tamaño+1):
    arr.append(i)
    
 print("Este es el arreglo a sumar",arr)
 res=suma(arr)

 print('La suma del array es', str(res))

else:
    print("el numero es mayor a mil, no se puede hacer la suma, colocar otro numero por favor ")
  
    





   
  


    
