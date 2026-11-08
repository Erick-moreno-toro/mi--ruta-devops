import os
import platform
print("=== Diagnóstico del Servidor ===")
print(f"Sistema Operativo: {platform.system()} {platform.release()}")
print(f"Procesador: {platform.processor()}")
print(f"Usuario ejecutando el proceso: {os.getlogin()}")
print(f"Ruta actual de trabajo: {os.getcwd()}")
print("================================")