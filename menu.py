def menu_1():
    print("""
-------------------------------
      ¿QUE PERFIL TIENES?
-------------------------------
[1]-ADMINISTRADOR 
[2]-USUARIO   
[3]-SALIR                                     
-------------------------------
""")

def menu_admin():
    print("""
------------------------------      
[1]-USUARIOS
[2]-PLANES
[3]-VENTAS
[4]-REPORTES 
[5]-CATEGORIA          
[6]-SALIR                 
------------------------------          
""")

def menuUsua_admin():
    print("""
------------------------------          
[1]-VER PERFILES
[2]-AÑADIR PERFILES
[3]-ELIMINAR PERFILES 
[4]-VOLVER
------------------------------        
""")
    
def menuPlans_admin(): 
    print("""
------------------------------
[1]-VER PLANES Y SERVICIOS
[2]-AÑADIR PLANES
[3]-ELIMINAR PLANES
[4]-AÑADIR SERVICIOS
[5]-ELIMINAR SERVICIOS
[6]-VOLVER
------------------------------        
""")

def menuVent_admin():
    print("""
------------------------------
[1]-VER VENTAS
[2]-CREAR VENTA
[3]-VER PRODUCTOS
[4]-AÑADIR PRODUCTOS
[5]-ELIMINAR PRODUCTOS
[6]-VOLVER 
""")       
    
def menuReport_admin():
    print("""
-------------------------------
[1]-VER REPORTES
[2]-CREAR REPORTE
[3]-ELIMINAR REPORTES
[4]-VOLVER
""")

def menuCatego_admin():
    print("""
-------------------------------------------------------
[1]-VER CLIENTES DE CATEGORIA
[4]-EDITAR CLIENTES DE CATEGORIA  
[5]-VOLVER         
-------------------------------------------------------  
""")               
def menu_usuario():
    print("""
------------------------------
[1]-NUEVO USUARIO
[2]-EDITAR USUARIO
[3]-ELIMINAR USUARIO
[4]-VER PLANES 
[5]-VER PRODUCTOS
[6]-REPORTAR
[7]-PROMOS PERSONAL 
[8]-SALIR
------------------------------                            
""")     

def pedir_opcion():
    opc = 0
    opc = int(input("INGRESE LA OPCCION DESEADA: "))
    print("--------------------------")
    return opc
    
#opcion para mostrar sub menu 
def pedirSubM_opcion():
    opc = 0
    opc = int(input("INGRESE LA OPCCION DESEADA: "))
    print("--------------------------")
    return opc

    



