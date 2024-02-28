print("Hola usuario, bienvenido a la selección de productos de la panaderia Carlos :D!")

print("""
por favor escoje cual es tu preferencia (el número)      
      """)

categoria=tuple((
"Dulce",
"Sal",
"Pastel"))

for i, val in enumerate(categoria):
    print(f"{i}. {val} {categoria[i]}")
option=int(input(""))
print(f"""
Usuario usted seleccionó la categoría {categoria[option]} """) 


if option == 0:
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
        for i, val in enumerate(ProductosDulces):
           print(f"""{i}. {val} ${ValorDulce[i]}""")
           opcion=int(input(""))
           cantidad=int(input("cuantos quiere: "))
           print(f"Usuario usted seleccionó el producto {ProductosDulces[opcion]} con un valor de ${ValorDulce[opcion]*cantidad}")
           dinero=int(input("Ingrese la cantidad de dinero disponible: "))
           vueltos=(ValorDulce[opcion]*cantidad)-dinero 
           if dinero>=ValorDulce[opcion]*cantidad:
              print(f"Usuario usted compro el producto {ProductosDulces[opcion]} con un valor de ${ValorDulce[opcion]*cantidad}, sus vueltos son ${vueltos}")
           else:
              print(f"Usuario el producto que desea comprar {ProductosDulces[opcion]} con un valor de ${ValorDulce[opcion]*cantidad} le hacen falta ${(-vueltos)} ")




elif option == 1:
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
     for i, val in enumerate(ProductosSal):
        print(f"""{i}. {val} ${ValorSal[i]}""")
        opcion=int(input(""))
        cantidad=int(input("cuantos quiere: "))
        print(f"Usuario usted seleccionó el producto {ProductosSal[opcion]} con un valor de ${ValorSal[opcion]*cantidad}")
        dinero=int(input("Ingrese la cantidad de dinero disponible: "))
        vueltos=(ValorSal[opcion]*cantidad)-dinero 
        if dinero>=ValorSal[opcion]*cantidad:
          print(f"Usuario usted compro el producto {ProductosSal[opcion]} con un valor de ${ValorSal[opcion]*cantidad}, sus vueltos son ${vueltos}")
        else:
          print(f"Usuario el producto que desea comprar {ProductosSal[opcion]} con un valor de ${ValorSal[opcion]*cantidad} le hacen falta ${(-vueltos)} ")



elif option == 2:
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
      "2x1 en pastel de torta de chocolate"
      "2x1 en pastel zanahoria"
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
      50000,
      40000,
      45000
      ))
      for i, val in enumerate(ProductosPasteles):
         print(f"""{i}. {val} ${ValorPastel[i]}""")
         
      opcion=int(input(""))
      cantidad=int(input("cuantos quiere: "))
      print(f"Usuario usted seleccionó el producto {ProductosPasteles[opcion]} con un valor de ${ValorPastel[opcion]*cantidad}")
      dinero=int(input("Ingrese la cantidad de dinero disponible: "))
      vueltos=(ValorPastel[opcion]*cantidad)-dinero
      if dinero>=ValorPastel[opcion]*cantidad:
        print(f"Usuario usted compro el producto {ProductosPasteles[opcion]} con un valor de ${ValorPastel[opcion]*cantidad}, sus vueltos son ${vueltos}")
      else:
        print(f"Usuario el producto que desea comprar {ProductosPasteles[opcion]} con un valor de ${ValorPastel[opcion]*cantidad} le hacen falta ${(-vueltos)} ")



