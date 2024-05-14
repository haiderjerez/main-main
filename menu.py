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
[2]-VER PRODUCTOS
[3]-AÑADIR PRODUCTOS
[4]-ELIMINAR PRODUCTOS
[5]-VOLVER 
""")       

def menuCatego_admin():
    print("""
-------------------------------------------------------
[1]-VER INTEGRANTES DE CATEGORIA 'NUEVOS CLIENTES'
[2]-VER INTEGRANTES DE CATEGORIA 'CLIENTES REGULARES'
[3]-VER INTEGRANTES DE CATEGORIA 'CLIENTES LEALES'
[4]-AÑADIR CLIENTES A CATEGORIA
[5]-ELIMINAR CLIENTES DE CATEGORIA  
[6]-VOLVER         
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
[8]-CATEGORIA   
[9]-SALIR
------------------------------                            
""")     

def pedir_opcion():
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
    
def pedirSubM_opcion():
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
    
