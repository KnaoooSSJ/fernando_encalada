import os
import shutil

# Definir rutas
source_folder = r"C:\ruta\de\origen"
backup_folder = r"C:\ruta\de\baks"
log_folder = r"C:\ruta\de\logs"

# Crear carpetas si no existen
os.makedirs(backup_folder, exist_ok=True)
os.makedirs(log_folder, exist_ok=True)

# Definir los nombres de los archivos
bak_file = "nombre_apellido.bak"
log_file = "nombre_apellido.log"

# Mover archivos .bak
source_bak_path = os.path.join(source_folder, bak_file)
destination_bak_path = os.path.join(backup_folder, bak_file)

if os.path.exists(source_bak_path):
    shutil.move(source_bak_path, destination_bak_path)
    print(f"Archivo movido: {bak_file} a {backup_folder}")
else:
    print(f"Archivo no encontrado: {bak_file}")

# Mover archivos .log
source_log_path = os.path.join(source_folder, log_file)
destination_log_path = os.path.join(log_folder, log_file)

if os.path.exists(source_log_path):
    shutil.move(source_log_path, destination_log_path)
    print(f"Archivo movido: {log_file} a {log_folder}")
else:
    print(f"Archivo no encontrado: {log_file}")