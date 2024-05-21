import os
import time, traceback
from datetime import datetime

# Capturar excepciones  
def capturarException(exception):
    # Obtener la fecha y hora actual
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Crear el mensaje de error con la fecha y hora
    mensaje_error = (f"Fecha y hora: {fecha_actual}\n")
    mensaje_error += traceback.format_exc()  # Agregar el traceback de la excepción
    
    # Guardar el mensaje de error en un archivo de texto
    with open("error.txt", "a") as file:
        file.write(mensaje_error + "\n")

    os.system("clear")
    print("----------------")        
    print("VALOR INCORRECTO")
    print("----------------")
    time.sleep(2)