#mostrar lista de usuarios

def mostrarLIST_usuario ():
    datos = mostrarLIST_usuario()
    for usuario in datos():
        print("-------------------------------")
        print("usuario")
        print("-------------------------------")
        return usuario

#eliminar usuario 
def eliminar_usuario(datos):
    documento =input("INGRESE EL DOCUMENTO A ELIMINAR: ")
    for i in range(len(datos["usuario"])):
        if datos["usuario"][i]["documento"] == documento:
           datos["usuario"].pop(i)
           print("EL USUARIO HA SIDO ELIMINADO")
           return datos
        
    print("EL DOCUMENTO NO ES EXISTENTE")
    return datos







