import math
a = float(input("Ingresa el valor de a: "))
b = float(input("Ingresa el valor de b: "))
c = float(input("Ingresa el valor de c: "))

raiz = (b**2)-(4*a*c)
if(raiz<0):
    x_real = (-b)/(2*a)
    x_ima = (math.sqrt(raiz*(-1)))/(2*a)
    if(x_ima<0):
        print("El valor de x1 es: "+str(x_real)+str(x_ima)+"i")
        print("El valor de x2 es: "+str(x_real)+"+"+str(x_ima*(-1))+"i")
    else:
        print("El valor de x1 es: "+str(x_real)+"+"+str(x_ima)+"i")
        print("El valor de x2 es: "+str(x_real)+"-"+str(x_ima)+"i")
elif(raiz>0):
    resRaiz = math.sqrt(raiz)
    x1 = (-b+resRaiz)/(2*a)
    x2 = (-b-resRaiz)/(2*a)
    print("El valor de x1 es: ",x1)
    print("El valor de x2 es: ",x2)
elif(raiz==0):
    x = (-b)/2*a
    print("El resultado de x es: ",x)