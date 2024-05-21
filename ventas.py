import json 
import os 

def mostrarVentas():
    with open("ventas.json","r") as json_file:
        data = json.load(json_file)
        os.system("clear") 
        if data == None:
            print("NO HAY VENTAS")  
        for ventas in data:
            print("-----------------------------------------------------------------")
            print("numero_de_venta",":", ventas["numero_de_venta"])
            print("precio",":", ventas["precio"])
            print("cantidad",":", ventas["cantidad"])
            print("direccion",":", ventas["direcion"])
            print("documento",":", ventas["documento"])
            print("descripcion",":", ventas["descripcion"])
            print("telefono",":", ventas["telefono"])
            print("categoria",":", ventas["categoria"])
            print("----------------------------------------------------------------")

#guardar los usuarios 
def guardarVenta(ventas):
    with open('ventas.json','w') as json_file:
        json.dump(ventas, json_file, indent=4)

#crear ventas
def crearVentas():
    os.system("cls")
    with open("ventas.json","r") as json_file:
        data = json.load(json_file)

    ventas={}
    ventas["numero_de_venta"]=input("INGRESE EL NUMERO DE LA VENTA: ")
    ventas["precio"]=input("INGRESE EL PRECIO DE LA VENTA: ")
    ventas["cantidad"]=input("INGRESE LA CANTIDAD VENDIDA: ")
    ventas["direccion"]=input("INGRESE LA DIRECCION: ")
    ventas["documento"]=input("INGRESE EL NUMERO DE DOCUMENTO DEL COMPRADOR: ")
    ventas["telefono"]=input("INGRESE EL NUMERO DE TELEFONO: ")
    ventas["categoria"]=input("INGRESE LA CATEGORIA DE LA VENTA: ")
    data.append(ventas)
    print("LA VENTA HA SIDO CREADO EXITOSAMENTE")
    guardarVenta(data)
    os.system("pause")
    return
