import json
import os

#mostrar los reportes
def mostrarLIST_reportes():
    with open("reportes.json","r") as json_file:
        data = json.load(json_file)
    for user in data:
        print("-----------------------------------------------------------------")
        print("nombre",":", user["nombre"])
        print("fecha",":", user["fecha"])
        print("descripcion",":", user["descripcion"])
        print("codigo",":", user["codigo"])

#guardar los reportes
def guardarReporte(reporte):
    with open('reportes.json','w') as json_file:
        json.dump(reporte, json_file, indent=4)

#crear reporte
def crearReporte():
    os.system("clear")
    with open("reportes.json","r") as json_file:
        data = json.load(json_file)

        report ={}
        report["nombre"] = input("INGRESE EL NOMBRE COMPLETO DE QUIEN VA HA HACER EL REPORTE: ")
        report["fecha"] = input("INGRESE LA FECHA DEL REPORTE: ")
        report["descripcion"] = input("INGRESE LA DESCRIPCION DEL REPORTE: ")
        report["codigo"] = input("INGRESE EL CODIGO DEL REPORTE: ")
    data.append(report)
    print("EL REPORTE HA SIDO CREADO EXITOSAMENTE")
    guardarReporte(data)
    os.system("pause")
    return

#eliminar reportes
def eliminarReporte():
    os.system("clear")
    with open("reportes.json","r") as json_file:
        data = json.load(json_file)

    codigo =input("INGRESE EL CODIGO DEL SERVICIO A ELIMINAR: ")
    for i in range(len(data)):
        if data[i]["codigo"] == codigo:
           data.pop(i)
           print("EL REPORTE HA SIDO ELIMINADO")
           guardarReporte(data)
           os.system("pause")
           return
        
