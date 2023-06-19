vehiculos= list()
def grabar():
    vehiculo=list()
    multas=list()
    print("Ingrese los datos del vehículo. ")
    tipo=input("Tipo de vehículo: ")
    vehiculo.append(tipo)
    patente=input("Patente: ")
    vehiculo.append(patente)
    marca=input("Marca: ")
    if 2<=len(marca)<=15:
        vehiculo.append(marca)
    else:
        print("El nombre es demasiado pequeño. ")
    precio=int(input("Precio: "))
    if precio>=5000000:
        vehiculo.append(precio)
    else:
        print("El valor del vehículo no es suficiente.")
    fecha_registro= input("Fecha de Registro: ")
    vehiculo.append(fecha_registro)
    nombre_dueño=input("Nombre dueño: ")
    vehiculo.append(nombre_dueño)
    print("¿Posee multas?")
    print("1. Si ")
    print("2. No ")
    op1=int(input())
    if op1== 1:
        monto_multa=int(input("Ingrese el monto de la multa: "))
        fecha_multa= input("Ingrese la Fecha de la multa: ")
        multas.append(monto_multa)
        multas.append(fecha_multa)
        vehiculo.append(multas)
    vehiculos.append(vehiculo)
 # Vehiculo=(tipo,patente,marca,precio,fecha_registro,nombre_dueño,(multas))
 # multas=(monto_multa,fecha_multa)   

def buscar():
    patente=input("Ingrese la pátente que desea buscar: ")
    for i in range(len(vehiculos)):
        if patente== vehiculos[i][1]:
            print(f"Tipo de vehículo: {vehiculos[i][0]}")
            print(f"Patente: {vehiculos[i][1]}")
            print(f"Marca: {vehiculos[i][2]}")
            print(f"Precio: {vehiculos[i][3]}")
            print(f"Fecha Registro: {vehiculos[i][4]}")
            print(f"Nombre Dueño: {vehiculos[i][5]} ")
            if vehiculos[i][6] is True:
                print("Multas: ")
                print(f"Monto multa: {vehiculos[i][6][0]}")
                print(f"Fecha multa: {vehiculos[i][6][1]}")

def certificados():
    patente=input("Ingrese la patente del vehículo: ")
    print("Certificados: ")
    print("1.- Emisión de Contaminantes. ($3.500)")
    print("2.- Certificado de anotaciones. ($2.000) ")
    print("3.- Certificado de multas: ($3.000) ")
    op3=int(input())
    for i in range(len(vehiculos)):
        if patente== vehiculos[i][1]:
            if op3==1:
                pago=3500
                print("Certificado de Emisión de contaminantes. ")
                print(f"Patente del vehículo: {vehiculos[i][1]}")
                print(f"Nombre del dueño: {vehiculos[i][5]}")
                print(f"Total a pagar: {pago}")
            elif op3==2:
                pago=2000
                print("Certificado de anotaciones. ")
                print(f"Patente del vehículo: {vehiculos[i][1]}")
                print(f"Nombre del dueño: {vehiculos[i][5]}")
                print(f"Total a pagar: {pago}")
            elif op3==3:
                pago=3000
                print("Certificado de anotaciones. ")
                print(f"Patente del vehículo: {vehiculos[i][1]}")
                print(f"Nombre del dueño: {vehiculos[i][5]}")
                print(f"Total a pagar: {pago}")

sw=0
while sw==0:
    print("Bienvenido(a) a Auto Seguro! ")
    print("1.- Grabar ")
    print("2.- Buscar  ")
    print("3.- Imprimir certificados  ")
    print("4.- Salir  ")
    op=int(input())
    if op==1:
        grabar()
    elif op==2:
        buscar()
    elif op==3:
        certificados()
    elif op==4:
        sw=1





