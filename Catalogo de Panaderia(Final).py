categoria = tuple(("Dulce", "Sal", "Pastel"))

for i, val in enumerate(categoria):print(f"{i}. {val}")

option = int(input("Seleccione una categoría (ingrese el número correspondiente): "))










if option == 0:
    ProductosDulces = ["Croissants", "Donas", "Tortillas", "Galletas", "Pan dulce","Ensaimadas", "Tartaletas", "Bizcochos", "Palmeras", "Conchas","Promo conchas x2", "Promo croissants x3"]
    ValorDulce = [3500, 2000, 60000, 1500, 7000, 5000, 6000, 45000, 2500, 2000, 3000, 7000]

    for i, val in enumerate(ProductosDulces):
        print(f"{i}. {val} ${ValorDulce[i]}")

    opcion = int(input("Seleccione un producto (ingrese el número correspondiente): "))
    cantidad = int(input("Ingrese la cantidad que desea comprar: "))
    total = ValorDulce[opcion] * cantidad

    print(f"Usted seleccionó el producto {ProductosDulces[opcion]} con un valor de ${total}")


    dinero = int(input("Ingrese la cantidad de dinero disponible: "))
    vuelto = dinero - total
    
    if dinero >= total:
        print(f"Usted compró el producto {ProductosDulces[opcion]} con un valor de ${total}, sus vueltos son ${vuelto}")
    else:
        print(f"Le falta dinero, necesita ${-vuelto} más para comprar este producto.")












if option==1:
    Productosal=["Baguettes"",Pan de masa madre","Pan de ajo","ocaccia","Pretzels","Bollos de queso","Empanadas","Pan de centeno","Pan de aceitunas,Pan de hierbas"]
    valoressal=[5000,6000,4000,8000,4500,2500,2000,5500,4500,4000]
















if option==2:
    Productospastel=["Torta de chocolate","Tarta de manzana","Torta de zanahoria (Carrot cake)","Torta Red Velvet","Tarta de limón","Torta de queso (Cheesecake)","Torta de frutas","Tarta Sacher (Sachertorte)","Torta de tres leches","Torta de nueces y caramelo (Sticky toffee cake)"]
    valorespastel=[40000,35000,45000,50000,40000,50000,45000,55000,40000,50000]










else:
    print("Opción no válida")