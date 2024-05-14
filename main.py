#imports

import agruparPorCategoria
import menu
import datos
import os
import usuarios
import pedirSubSubM_opcion
import planes
import pedirSubMplan_opcion
import servicios
import pedirSubMventas_opcion
import productos
import pedirSubMreport_opcion
import reportes
import pedirSubMcategoria_opcion
import agruparPorCategoria
import pedirSubMusuario_opcion



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
                        print(usuarios.mostrarLIST_usuario())
                    elif opc == 2:
                        usuarios.crearUsuario()
                    elif opc == 3:
                        usuarios.eliminarUsuario()
                    elif opc == 4:
                        menu.menu_admin()
                elif opc == 2:
                    menu.menuPlans_admin()
                    opc=pedirSubMplan_opcion.pedirSubMplan_opcion()
                    if opc == 1:
                        print(planes.mostrarLIST_planes())
                    elif opc == 2: 
                        planes.crearPlanes()
                    elif opc == 3:
                        planes.eliminarPlanes()
                    elif opc == 4:
                        servicios.crearServicios()
                    elif opc == 5:
                        servicios.eliminarServicios()
                    elif opc == 6:
                        menu.menu_admin()
                elif opc == 3:
                    menu.menuVent_admin()
                    opc=pedirSubMventas_opcion.pedirSubMventas_opcion()
                    if opc == 1:
                        print("ver ventas")
                    elif opc == 2:
                        print(productos.mostrarLIST_productos())
                    elif opc ==3:
                        productos.crearProductos()
                    elif opc == 4:
                        productos.eliminarProductos()
                    elif opc == 5:
                        menu.menu_admin()
                elif opc == 4:
                    menu.menuReport_admin()
                    opc=pedirSubMreport_opcion.pedirSubMreport_opcion()
                    if opc == 1:
                        print (menu.menuReport_admin)
                    elif opc == 2:
                        reportes.eliminarReporte()
                    elif opc == 3:
                        menu.menu_admin()
                elif opc== 5:
                    menu.menuCatego_admin()
                    opc=pedirSubMcategoria_opcion.pedirSubMcategoria_opcion()
                    if opc == 1:
                        agruparPorCategoria.agruparPorCategoria()
                    elif opc == 2:
                        usuarios.editarCategoria()
                    elif opc == 3:
                        menu.menu_admin()
                elif opc == 6:
                    break 
            elif opc == 2:
                menu.menu_usuario()
                opc=pedirSubMusuario_opcion.pedirSubMusuario_opcion()
                if opc == 1:
                    usuarios.crearUsuario_usu()
                elif opc == 2:
                    usuarios.editarUsuarios()
                elif opc == 3:
                    usuarios.eliminarUsuario()
                elif opc == 4:
                    planes.mostrarLIST_planes()
                elif opc == 5:
                    productos.mostrarLIST_productos()
                elif opc == 6:
                    reportes.crearReporte()
                elif opc == 7:
                    usuarios.promoPersonal()
                elif opc == 8:
                    menu.menu_1()
            elif opc == 3:
                print("GRACIAS POR USAR EL SISTEMA")
            break
            
    except ValueError:
        print("Opcion no válida")
        os.system("clear")