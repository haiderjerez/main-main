import json
import os 
#mostrar los productos
def mostrarLIST_productos():
    with open("productos.json","r") as json_file:
        data = json.load(json_file)
    for user in data:
        print("-----------------------------------------------------------------")
        print("nombre",":", user["nombre"])
        print("precio",":", user["precio"])
        print("cantidad",":", user["cantidad"])
        print("descripcion",":", user["descripcion"])
        print("codigo",":", user["codigo"])
        print("categoria",":", user["categoria"])
        print("----------------------------------------------------------------")

#guardar productos 
def guardarProductos(productos):
    with open('productos.json','w') as json_file:
        json.dump(productos, json_file, indent=4)

#crear un producto 
def crearProductos():
    os.system("cls")
    with open("productos.json","r") as json_file:
        data = json.load(json_file)

    producto={}
    producto["nombre"]=input("INGRESE EL NOMBRE DEL PRODUCTO: ")
    producto["precio"]=input("INGRESE EL PRECIO DEL PRODUCTO: ")
    producto["cantidad"]=input("INGRESE LA CANTIDAD DEL PRODUCTO: ")
    producto["descripcion"]=input("INGRESE LA DESCRIPCION DEL PRODUCTO: ")
    producto["codigo"]=input("INGRESE EL CODIGO DEL PRODUCTO: ")
    producto["categoria"]=input("INGRESE LA CATEGORIA DEL PRODUCTO: ")
    data.append(producto)
    print("EL PRODUCTO HA SIDO CREADO EXITOSAMENTE")
    guardarProductos(data)
    os.system("pause")
    return

#eliminar productos
def eliminarProductos():
    os.system("cls")
    with open("productos.json","r") as json_file:
        data = json.load(json_file)

    codigo =input("INGRESE EL CODIGO DEL PLAN A ELIMINAR: ")
    for i in range(len(data)):
        if data[i]["codigo"] == codigo:
           data.pop(i)
           print("EL PRODUCTO HA SIDO ELIMINADO")
           guardarProductos(data)
           os.system("pause")
           return
    