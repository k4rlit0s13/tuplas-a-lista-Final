print("Hola usuario, bienvenido a la selección de productos de la panaderia Carlos :D!")

print("""
por favor escoje cual es tu preferencia (el número)      
      
      """)

categoria=tuple((
"Dulce",
"Sal",
"Pastel"))

for i, val in enumerate(categoria):
    print(f"""{i}. {val} {categoria[i]}""")
print("")
option=int(input(""))
print(f"""
Usuario usted seleccionó la categoría {categoria[option]} """) 








ProductosDulces=tuple((
"Croissants",
"Donas",
"Pasteles",
"Galletas",
"Pan dulce",
"Ensaimadas",
"Tartaletas",
"Bizcochos",
"Palmeras",
"Conchas",))

ValorDulce=tuple((
3500,
2000, 
60000, 
1500, 
7000, 
5000, 
6000, 
45000, 
2500, 
2000,
))

for i, val in enumerate(ProductosDulces):
    print(f"""{i}. {val} ${ValorDulce[i]}""")
#para un listado completo con detalle y decorado
    
opcion=int(input( ))
print(f"Usuario usted seleccionó el producto {ProductosDulces[opcion]} con un valor de ${ValorDulce[opcion]}") 
#para decir que el usuario seleccion
    
dinero=int(input("Ingrese la cantidad de dinero disponible: ")) #para pedirle la plata al usuario
    
vueltos=ValorDulce[opcion]-dinero
    
if dinero>=ValorDulce[opcion]:
        print(f"Usuario usted compro el producto {ProductosDulces[opcion]} con un valor de ${ValorDulce[opcion]}, sus vueltos son ${vueltos}")
    
else:
        print(f"Usuario el produtcto que desea comprar {ProductosDulces[opcion]} con un valor de ${ValorDulce[opcion]}l hacen falta ${(-vueltos)} ")









ProductosSal=tuple((
"Baguettes",
"Pan de masa madre",
"Pan de ajo",
"Focaccia",
"Pretzels",
"Bollos de queso",
"Empanadas",
"Pan de centeno",
"Pan de aceitunas",
"Pan de hierbas",
))

ValorSal=tuple((
5000,
6000,
4000,
8000,
3500,
2500,
2000,
5500,
4500,
4000,
))
for i, val in enumerate(ProductosDulces):
    print(f"""{i}. {val} ${ValorDulce[i]}""")
#para un listado completo con detalle y decorado
    
opcion=int(input( ))
print(f"Usuario usted seleccionó el producto {ProductosDulces[opcion]} con un valor de ${ValorDulce[opcion]}") 
#para decir que el usuario seleccion
    
dinero=int(input("Ingrese la cantidad de dinero disponible: ")) #para pedirle la plata al usuario
    
vueltos=ValorDulce[opcion]-dinero
    
if dinero>=ValorDulce[opcion]:
        print(f"Usuario usted compro el producto {ProductosDulces[opcion]} con un valor de ${ValorDulce[opcion]}, sus vueltos son ${vueltos}")
    
else:
        print(f"Usuario el produtcto que desea comprar {ProductosDulces[opcion]} con un valor de ${ValorDulce[opcion]}l hacen falta ${(-vueltos)} ")






ProductosPasteles=tuple((
"Torta de chocolate",
"Tarta de manzana",
"Torta de zanahoria (Carrot cake)",
"Torta Red Velvet",
"Tarta de limón",
"Torta de queso (Cheesecake)",
"Torta de frutas",
"Tarta Sacher (Sachertorte)",
"Torta de tres leches",
"Torta de nueces y caramelo (Sticky toffee cake)",
))

ValorPastel=tuple((
40000,
35000,
45000,
50000,
40000,
50000,
45000,
55000,
40000,
50000
))

for i, val in enumerate(ProductosDulces):
    print(f"""{i}. {val} ${ValorDulce[i]}""")
#para un listado completo con detalle y decorado
    
opcion=int(input( ))
print(f"Usuario usted seleccionó el producto {ProductosDulces[opcion]} con un valor de ${ValorDulce[opcion]}") 
#para decir que el usuario seleccion
    
dinero=int(input("Ingrese la cantidad de dinero disponible: ")) #para pedirle la plata al usuario
    
vueltos=ValorDulce[opcion]-dinero
    
if dinero>=ValorDulce[opcion]:
        print(f"Usuario usted compro el producto {ProductosDulces[opcion]} con un valor de ${ValorDulce[opcion]}, sus vueltos son ${vueltos}")
    
else:
        print(f"Usuario el produtcto que desea comprar {ProductosDulces[opcion]} con un valor de ${ValorDulce[opcion]}l hacen falta ${(-vueltos)} ")



