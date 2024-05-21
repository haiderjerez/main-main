import json 
import os

#mostrar planes
def mostrarLIST_planes():
    with open("planes.json","r") as json_file:
        data = json.load(json_file)
    for user in data:
        print("-----------------------------------------------------------------")
        print("nombre",":", user["nombre"])
        print("precio",":", user["precio"])
        print("descripcion",":", user["descripcion"])
        print("duracion",":", user["duracion"])
        print("codigo",":", user["codigo"])

#guardar los planes
def guardarPlanes(planes):
    with open('planes.json','w') as json_file:
        json.dump(planes, json_file, indent=4)

#crear planes
def crearPlanes():
    os.system("cls")
    with open("planes.json","r") as json_file:
        data = json.load(json_file)

    planes={}
    planes["nombre"] = input("INGRESE EL NOMBRE DEL PLAN: ")
    planes["precio"] = input("INGRESE EL PRECIO DEL PLAN: ")
    planes["descripcion"] = input("INGRESE LA DESCRIPCION DEL PLAN: ")
    planes["duracion"] = input("INGRESE LA DURACION DEL PLAN: ")
    planes["codigo"] = input("INGRESE EL CODIGO DEL PLAN: ")
    data.append(planes)
    print("EL PLAN HA SIDO CREADO EXITOSAMENTE")
    guardarPlanes(data)
    os.system("pause")
    return

#eliminar planes
def eliminarPlanes():
    os.system("cls")
    with open("planes.json","r") as json_file:
        data = json.load(json_file)

    codigo =input("INGRESE EL CODIGO DEL PLAN A ELIMINAR: ")
    for i in range(len(data)):
        if data[i]["codigo"] == codigo:
           data.pop(i)
           print("EL PLAN HA SIDO ELIMINADO")
           guardarPlanes(data)
           os.system("pause")
           return