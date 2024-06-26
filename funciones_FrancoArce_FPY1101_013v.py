import os
libros={}
prestamo={}
prestados=[]
def reg_libro():
    titulo=input("Ingrese el Titulo del libro: ")
    autor=input("Ingrese el autor del libro: ")
    try:
        año=int(input("Ingrese el año de publicacion:"))
    except ValueError:
        año=False
    sku=input("Ingrese el SKU del libro (las 6 primeras letras del título del libro – las 3 primeras letras del autor – año de publicación.): ")
    if titulo and autor and año and sku:
        libros[titulo]={"autor":autor,"año":año,"sku":sku}
        print("Libro registrado exitosamente.")
    else:
        print("Algun dato ingresado incorrectamente, reintente.")

def prestar_libro():
    usuario=input("Ingrese usuario: ")
    sku=input("Ingrese SKU del libro: ")
    fecha=input("Ingrese fecha de prestamo: ")
    libre=True
    libro=False
    for titulo, datos in libros.items():
        if datos['sku']==sku:
            libro=True
            prest=titulo
    if sku in prestados:
        libre=False
    if libro and libre and fecha:
        prestamo[usuario]={"sku":sku, "fecha":fecha, "titulo":prest} 
        prestados.append(sku)
        print("Prestamo realizado") 
    else:
        print("El libro fue prestado o no se encuentra registrado.")

def lista_todos():
    print("TITULO\tAUTOR\tAÑO DE PUBLICACION\tSKU\n")
    for titulo, datos in libros.items():
        print(f"{titulo}\t{datos['autor']}\t{datos['año']}\t\t{datos['sku']}\n")

def reporte():
    with open(f"Reporte_Prestamos.txt","w") as file:
        file.write(f"USUARIO\tTITULO\tFECHA DE PRESTAMO\n")
        for usuario, datos in prestamo.items():
            file.write(f"{usuario}\t{datos['titulo']}\t{datos['fecha']}\n")
    print(f"El archivo fue generado exitosamente en la carpeta: {os.getcwd()}" )
