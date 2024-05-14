def registra_usuario(datos):
    usuario={}
    usuario["primer_nombre"]=input("INGRESE SU NOMBRE: ")
    usuario["segundo_nombre"]=input("INGRESE SU SEGUNDO NOMBRE: ")
    usuario["primer_apellido"]=input("INGRESE SU PRIMER APELLIDO: ")
    usuario["segundo_apellido"]=input("INGRESE SU SEGUNDO APELLIDO: ")
    usuario["direccion"]=input("INGRESE SU DIRECCION: ")
    usuario["tipo_documento"]=input("INGRESE TIPO DE DOCUMENTO TIENE: ")
    usuario["cedula"]=input("INGRESE SU NUMERO DE DOCUMENTO: ")
    usuario["numero"]=input("INGRESE SU NUMERO DE TELEFONO: ")
    datos["usuario"].append(usuario)
    print("REGISTRO EXITOS")
    return datos