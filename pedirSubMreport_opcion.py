#opcion reportes
def pedirSubMreport_opcion():
    opc = 0
    try:
        opc = int(input("INGRESE LA OPCCION DESEADA: "))
        print("--------------------------")
        return opc
    except Exception:
        print("""
OPCION NO VALIDA
""")
        return -1