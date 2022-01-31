import numpy as np

Lista_palabras=["I","N","O","S"]
Lista_num=[0,1,2,3]

print("Bienvenidos al cifrado de Hill")
print("Vamos a trabajar en encriptar pequeñas palabras como SI")
print("Para esto primero tenemos que convertirlas en números con las siguiente tabla equivalente: \n")
print(Lista_palabras)
print(Lista_num)
input("")

print("Como podemos observar nuestra palabra [S   I] seria equivalente a los números [3   0]")
print("Ahora comenzemos a cifrar!")
input("")

print(" ")
prueba=[7,2,3,1]
V_prueba=np.array(prueba)
M_llave=V_prueba.reshape(2,2)
print("Aqui tiene su matriz llave: \n")
arr = [[7, 2],
       [3, 1],]
for i in arr:
    print("|"+'\t'.join(map(str, i)) + "|")

prueba1=[3,0]
V_prueba1=np.array(prueba1)
#print(V_prueba1)
M_palabra1=V_prueba1.reshape(2,1)
print("Su codigo a encriptar: \n")
arr = [[3],
       [0],]
for i in arr:
    print("|"+'\t'.join(map(str, i)) + "|")



prueba2=["3x7","3x3"]
V_prueba2=np.array(prueba2)
M_mult1=V_prueba2.reshape(2,1)
print("Realice las siguientes operaciones para encriptar \n")
arr = [[3, "x", 7],
       [3, "x", 3],]
for i in arr:
    print("|"+'\t'.join(map(str, i)) + "|")

resp1=0
while(resp1 != 21):
  resp1= int(input("El primer valor de 3x7 es:"))

resp2=0
while(resp2 != 9):
  resp2= int(input("El segundo valor de 3x3 es:"))

prueba3=[21,9]
V_prueba3=np.array(prueba3)
M_cif1=V_prueba3.reshape(2,1)

print("Felicidades cifraste tu codigo con el resultado de : \n")

arr = [[21],
       [" 9"],]
for i in arr:
    print("|"+'\t'.join(map(str, i)) + "|")

input("")

print("Ahora ayudanos modulando el código con esta tabla \n 5x4 mod 4 = 0 \n 7x3 mod 4 = 1 \n 11x2 mod 4= 2 \n 2x4 mod 4 = 0 \n 3x3 mod 4= 1 \n 5x2 mod 4 = 2")
resp3=0
while (resp3 != 1):
  resp3= int(input("El resultado de 21 mod 4 es:"))

resp4=0
while (resp4 !=1):
  resp4=int(input("El resultado de 9 mod 4 es: "))

print("Felicidades! vamos por buen camino")
input("")
print("Ahora ayudanos decifrando tu código")

inv=[1,-2,-3,7]
V_inv=np.array(inv)
M_inv=V_inv.reshape(2,2)

cod=[1,1]
V_cod=np.array(cod)
M_cod=V_cod.reshape(2,1)

proc2=["1-2","-3+7"]
V_proc2=np.array(proc2)
M_proc2=V_proc2.reshape(2,1)

print("Con nuestra matriz llave invertida \n")

arr = [[1,-2],
       [-3," 7"],]
for i in arr:
    print("|"+'\t'.join(map(str, i)) + "|")

print("Tu código encriptado: \n")

arr = [[1],
       [1],]
for i in arr:
    print("|"+'\t'.join(map(str, i)) + "|")

input()
print("Realice las siguientes sumas y restas para comenzar a desencriptar \n")
arr = [[1,"-",2],
       [-3,"+",7],]
for i in arr:
    print("|"+'\t'.join(map(str, i)) + "|")

resp5=0
while(resp5 != -1):
  resp5= int(input("La respuesta de 1-2 es:"))

resp6=0
while(resp6 != 4):
  resp6= int(input("La respuesta de -3+7 es:"))

print("Buen trabajo! Ya mismo terminamos la decodificación")
input("")
print("Ahora ayudanos modulando nuevamente el decifrado con la siguiente tabla:\n -2x1 mod 4= 2 \n -1x1 mod 4 = 3 \n 0 mod 4 = 0 \n 3x1 mod 4 = 3 \n 1x4 mod 4 = 0 \n 5x1 mod 4 = 1")

resp7=0
while (resp7 != 3):
  resp7= int(input("El resultado de -1 mod 4 es:"))

  resp8=-1
while (resp8 != 0):
  resp8= int(input("El resultado de 4 mod 4 es:"))

print("Excelente! Al decodificar tu código obtuvista como resultado: \n", M_palabra1)

print("Que es la misma Matriz que codificamos al comienzo")
print("Si observamos nuestra tabla de conversión de números a letras y viceversa")
print(Lista_palabras)
print(Lista_num)
print("Es la palabra SI")


#print(str(M_llave), str(M_prueba))



# np.linalg.inv()

#print(M_llave, "\t", M_prueba)
#print(M_prueba)
