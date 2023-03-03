#Area de un circulo
#definimos una variable y pedimos al usuario que ingrese el valor del radio
radio = float(input("Ingrese el  valor del radio: "))
#importamos la libreria math
from math import pi
#Proceso para hallar el area del circulo
area_circulo = pi *radio**2
#mostramos el area
print("El área del circulo es :",area_circulo)