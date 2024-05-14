#imports

import menu
import datos
import os

import pedirSubSubM_opcion
from registra_usuario import registra_usuario
from usuarios import eliminar_usuario, mostrarLIST_usuario


#constants
RUTA_BASE_DE_DATOS = "usuario.json"

datos = datos.cargar_datos(RUTA_BASE_DE_DATOS)

while True:
    try:
        menu.menu_1()
        while True:
            opc = menu.pedir_opcion()
            if opc == 1:
                menu.menu_admin()
                opc=menu.pedirSubM_opcion()
                if opc ==1:
                    menu.menuUsua_admin()
                    opc=pedirSubSubM_opcion.pedirSubSubM_opcion()
                    if opc == 1:
                        print(mostrarLIST_usuario())
                    elif opc == 2:
                        datos = (registra_usuario(datos))
                    elif opc == 3:
                        datos = (eliminar_usuario(datos))
                elif opc == 2:
                    menu.menuPlans_admin()
                elif opc == 3:
                    menu.menuVent_admin()
                elif opc == 4:
                    print("palo")
                elif opc== 5:
                    menu.menuCatego_admin()
                elif opc == 6:
                    break 
            elif opc == 2:
                menu.menu_usuario()

            elif opc == 3:
                print("GRACIAS POR USAR EL SISTEMA")
                break
        guardar_datos(datos, RUTA_BASE_DE_DATOS)  # noqa: F821
            
    except ValueError:
        print("Opcion no valida")
        os.system("clear")

        

