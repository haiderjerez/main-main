from ast import Return
import json
import os
from tarfile import data_filter 

#mostrar lista de usuarios
def mostrarLIST_usuario():
    with open("usuario.json","r") as json_file:
        data = json.load(json_file) 
        for user in data:
            print("-----------------------------------------------------------------")
            print("nombre",":", user["primer_nombre"])
            print("apellido",":", user["primer_apellido"])
            print("direccion",":", user["direccion"])
            print("tipo_documento",":", user["tipo_documento"])
            print("documento",":", user["documento"])
            print("telefono",":", user["telefono"])
            print("categoria",":", user["categoria"])
            print("----------------------------------------------------------------")


#guardar los usuarios 
def guardarUsuarios(usuarios):
    with open('usuario.json','w') as json_file:
        json.dump(usuarios, json_file, indent=4)

#crear los usuarios_admin
def crearUsuario_admin():
    os.system("cls")
    with open("usuario.json","r") as json_file:
        data = json.load(json_file)

    usuario={}
    usuario["primer_nombre"]=input("INGRESE SU NOMBRE: ")
    usuario["segundo_nombre"]=input("INGRESE SU SEGUNDO NOMBRE: ")
    usuario["primer_apellido"]=input("INGRESE SU PRIMER APELLIDO: ")
    usuario["segundo_apellido"]=input("INGRESE SU SEGUNDO APELLIDO: ")
    usuario["direccion"]=input("INGRESE SU DIRECCION: ")
    usuario["tipo_documento"]=input("INGRESE TIPO DE DOCUMENTO TIENE: ")
    usuario["documento"]=input("INGRESE SU NUMERO DE DOCUMENTO: ")
    usuario["telefono"]=input("INGRESE SU NUMERO DE TELEFONO: ")
    usuario["categoria"]=input("INGRESE LA CATEGORIA QUE VA ESTE CLIENTE: ")
    data.append(usuario)
    print("EL USUARIO HA SIDO CREADO EXITOSAMENTE")
    guardarUsuarios(data)
    os.system("pause")
    return

#eliminar usuarios
def eliminarUsuario():
    os.system("cls")
    with open("usuario.json","r") as json_file:
        data = json.load(json_file)

    documento =input("INGRESE EL DOCUMENTO A ELIMINAR: ")
    for i in range(len(data)):
        if data[i]["documento"] == documento:
           data.pop(i)
           print("EL USUARIO HA SIDO ELIMINADO")
           guardarUsuarios(data)
           os.system("pause")
           return

#crear usuarios
def crearUsuario_usu():
    os.system("cls")
    with open("usuario.json","r") as json_file:
        data = json.load(json_file)

    usuario={}
    usuario["primer_nombre"]=input("INGRESE SU NOMBRE: ")
    usuario["segundo_nombre"]=input("INGRESE SU SEGUNDO NOMBRE: ")
    usuario["primer_apellido"]=input("INGRESE SU PRIMER APELLIDO: ")
    usuario["segundo_apellido"]=input("INGRESE SU SEGUNDO APELLIDO: ")
    usuario["direccion"]=input("INGRESE SU DIRECCION: ")
    usuario["tipo_documento"]=input("INGRESE TIPO DE DOCUMENTO TIENE: ")
    usuario["documento"]=input("INGRESE SU NUMERO DE DOCUMENTO: ")
    usuario["telefono"]=input("INGRESE SU NUMERO DE TELEFONO: ")
    data.append(usuario)
    print("EL USUARIO HA SIDO CREADO EXITOSAMENTE")
    guardarUsuarios(data)
    os.system("pause")
    return


#editar usuarios
def editarUsuarios():
    os.system("cls")
    with open("usuario.json","r") as json_file:
        data = json.load(json_file)

        documento =input("INGRESE EL DOCUMENTO A EDITAR: ")
        for i in range(len(data)):
            if data[i]["documento"] == documento:
                nuevo_primerNombre = input("INGRESE EL NUEVO PRIMER NOMBRE: ")
                nuevo_segundoNombre = input("INGRESE EL NUEVO SEGUNDO NOMBRE: ")
                nuevo_primerApellido = input("INGRESE EL NUEVO PRIMER APELLIDO: ")
                nuevo_segundoApellido = input("INGRESE EL NUEVO SEGUNDO APELLIDO: ")
                nuevo_direccion = input("INGRESE LA NUEVA DIRECCION: ")
                nuevo_tipoDocumento = input("INGRESE EL NUEVO TIPO DE DOCUMENTO: ")
                nuevo_telefono = input("INGRESE EL NUEVO NUMERO DE TELEFONO: ")

                data[i]["primer_nombre"] = nuevo_primerNombre
                data[i]["segundo_nombre"] = nuevo_segundoNombre
                data[i]["primer_apellido"] = nuevo_primerApellido
                data[i]["segundo_apellido"] = nuevo_segundoApellido
                data[i]["direccion"] = nuevo_direccion
                data[i]["tipo_documento"] = nuevo_tipoDocumento
                data[i]["telefono"] = nuevo_telefono
                print("EL USUARIO HA SIDO EDITADO")
                break
            else:
                print("EL DOCUMENTO NO EXISTE")
    with open("usuario.json", "w") as json_file:
            json.dump(data, json_file, indent=4) # type: ignore  # noqa: F821
 
#editar la categoria
def editarCategoria():
    os.system("cls")
    with open("usuario.json","r") as json_file:
        data = json.load(json_file)

    documento =input("INGRESE EL DOCUMENTO A EDITAR: ")
    for i in range(len(data)):
        if data[i]["documento"] == documento:
           data[i]["categoria"]=input("INGRESE LA NUEVA CATEGORIA: ")
           print("LA CATEGORIA HA SIDO EDITADA")
           guardarUsuarios(data)
           os.system("pause")
           return

#promo personal
def promoPersonal():
    os.system("cls")
    with open("usuario.json","r") as json_file:
        data = json.load(json_file)
        premios_regular=["TARJETA DE NETFLIX","TARJETA DE PARAMOUNT","TARJETA DE PRIMME VIDEO","DESCUENTO DEL 50%","DESCUENTO DEL 20%","DESCUENTO DEL 35%"]
        premios_leal=["PS5","PS4","XBOX SERIES X","CASCO PARA MOTO","TV","COMPUTARDOR","CELULAR","LABADORA","NEVERA"]
        
        documento = input("DIGUITE SU DOCUMENTO: ")
        for i in range(len(data)):

            if ["categoria"] == ["nuevo"]:
                print("TIENES QUE SUBIR DE RANGO EN NUESTRA TIENDA PARA PODER UTILIZAR ESTA OPCION")
            elif ["categoria"] == ["regular"]:
                premio_aleatorio=ramdom.choice(premios_regular) # type: ignore  # noqa: F821
                print("EL PREMIO ALEATORIO POR SU REGULAR LEALTAD SE HA GANADO", premio_aleatorio)
            elif ["categoria"] == ["leal"]:
                premio_aleatorio=ramdom.choice(premios_leal) # type: ignore  # noqa: F821
                print("EL PREMIO ALEATORIO POR SU LEALTAD SE HA GANADO", premio_aleatorio)
            else:
                print("EL NUMERO DE DOCUMENTO NO EXISTE")
            

        


