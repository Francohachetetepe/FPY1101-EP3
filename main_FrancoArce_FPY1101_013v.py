from funciones_FrancoArce_FPY1101_013v import * 
libros={}
prestamo={}
prestados=[]
print("Bienvenido.-")
while True:
    opc=input("\n1. Registrar libro\n2. Prestar libro\n3. Listar todos los libros\n4. Imprimir reporte de préstamos\n5. Salir del Programa\n")
    if opc=="1":
        reg_libro()
    elif opc=="2":
        prestar_libro()
    elif opc=="3":
        lista_todos()
    elif opc=="4":
       reporte()
    elif opc=="5":
        print("Programa Finalizado...\nDesarrollado por Franco Arce Moraga\nRUN: 19.225.867-7")
        break
    else:
        print("Opcion invalida")
