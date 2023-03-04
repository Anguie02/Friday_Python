#Progrma que permita imprimir el primer y ultimo  valor de la lista
#Pedimos el ingreso de los elementos para la lista
datos =input("Ingrese los datos separados:")
lista = datos.split()
#Imprimimos el primer y ultimo elemento
print("El primer elemento es :", lista[0], "y el úlimo es: ", lista[len(lista)-1])
