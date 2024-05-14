import json
import os


def agruparPorCategoria():
    os.system("cls")
    with open("usuario.json","r") as json_file:
        data = json.load(json_file)
        print("LAS CATEGORIAS SON: [NUEVO],[REGULAR],[LEAL].")

    categoria =input("INGRESE LA CATEGORIA QUE DESEA VER: ")
    for i in range(len(data)):
        if data[i]["categoria"] == categoria:
           print(data[i]["primer_nombre"])
           print(data[i]["segundo_nombre"])
           print(data[i]["primer_apellido"])
           print(data[i]["segundo_apellido"])
           print(data[i]["direccion"])
           print(data[i]["tipo_documento"])
           print(data[i]["documento"])
           print(data[i]["telefono"])
           print(data[i]["categoria"])
           os.system("pause")
           return