import json 
import os

#guardar los servicios 
def guardarServicios(planes):
    with open('planes.json','w') as json_file:
        json.dump(planes, json_file, indent=4)

#crear servicios
def crearServicios():
    os.system("cls")
    with open("planes.json","r") as json_file:
        data = json.load(json_file)

    servicios={}
    servicios["nombre"] = input("INGRESE EL NOMBRE DEL SERVICIO: ")
    servicios["precio"] = input("INGRESE EL PRECIO DEL SERVICIO: ")
    servicios["descripcion"] = input("INGRESE LA DESCRIPCION DEL SERVICIO: ")
    servicios["duracion"] = input("INGRESE LA DURACION DEL SERVICIO: ")
    servicios["codigo"] = input("INGRESE EL CODIGO DEL SERVICIO: ")
    data.append(servicios)
    print("EL SERVICIO HA SIDO CREADO EXITOSAMENTE")
    guardarServicios(data)
    os.system("pause")
    return

#eliminar servicios
def eliminarServicios():
    os.system("cls")
    with open("planes.json","r") as json_file:
        data = json.load(json_file)

    codigo =input("INGRESE EL CODIGO DEL SERVICIO A ELIMINAR: ")
    for i in range(len(data)):
        if data[i]["codigo"] == codigo:
           data.pop(i)
           print("EL SERVICIO HA SIDO ELIMINADO")
           guardarServicios(data)
           os.system("pause")
           return
        
