from dotenv import load_dotenv , find_dotenv

# imprime ubicacion del archivo .env
print(find_dotenv())

if load_dotenv(find_dotenv()):
    print("Claves cargadas con exito")
else:
    print("fallo carga de archivo claves")

# las claves se cargan como variables de entorno del sistema durante la execucion del script
    
import os
print(os.environ)
print(os.environ["NOMBRE"])