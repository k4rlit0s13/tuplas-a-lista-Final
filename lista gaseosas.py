productos = tuple((
"Coca-Cola",
"Pepsi",
"Sprite",
"Fanta",
"7UP",
"Mountain Dew",
"Dr Pepper",
"Schweppes",
"Mirinda",
"Lift"))
precios = tuple((
4500,
3750,
3000,
3600,
5250,
6000,
5400,
3900,
4200,
4800))


#for i in productos:  #para un listado normal
#    print(i)

#for i,val in enumerate(productos):  #para un listado completo con todos los datos
#    print(i,val,precios[i])

for i, val in enumerate(productos):
    print(f"""{i}. {val} ${precios[i]}""")
#para un listado completo con detalle y decorado
    
opcion=int(input( ))
print(f"Usuario usted seleccionó el producto {productos[opcion]} con un valor de ${precios[opcion]}") 
#para decir que el usuario seleccion
    
dinero=int(input("Ingrese la cantidad de dinero disponible: ")) #para pedirle la plata al usuario
    
vueltos=precios[opcion]-dinero
    
if dinero>=precios[opcion]:
        print(f"Usuario usted compro el producto {productos[opcion]} con un valor de ${precios[opcion]}, sus vueltos son ${vueltos}")
    
else:
        print(f"Usuario el produtcto que desea comprar {productos[opcion]} con un valor de ${precios[opcion]}l hacen falta ${(-vueltos)} ")

