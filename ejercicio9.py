import math

x1=float(input("Ingrese el  valor de (X1):   "))
x2=float(input("Ingrese el  valor de (X2):   "))
y1=float(input("Ingrese el  valor de (Y1):   "))
y2=float(input("Ingrese el  valor de (Y2):   "))

d = math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))

print(d)
