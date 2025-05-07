import os
from zipfile import ZipFile

# Define el directorio del proyecto
project_path = r"C:\Users\X1504Za 1 TB\Desktop\TALLER7\Proyecto_Web"

# Guardar nuevos archivos
contact_html = "<html><body>Contenido de ejemplo</body></html>"
contact_css = "body { font-family: Arial; }"
contact_js = "console.log('Archivo JS de ejemplo');"

os.makedirs(project_path, exist_ok=True)  # Crear el directorio si no existe

with open(f"{project_path}/contact.html", "w") as f:
    f.write(contact_html)

with open(f"{project_path}/contact.css", "w") as f:
    f.write(contact_css)

with open(f"{project_path}/contact.js", "w") as f:
    f.write(contact_js)

# Reempaquetar el proyecto en un nuevo archivo ZIP
extended_zip_path = r"C:\Users\X1504Za 1 TB\Desktop\TALLER7\Proyecto_Web_Extendido.zip"
with ZipFile(extended_zip_path, 'w') as zipf:
    for root, _, files in os.walk(project_path):
        for file in files:
            file_path = os.path.join(root, file)
            zipf.write(file_path, arcname=os.path.relpath(file_path, project_path))

print(f"Archivo ZIP creado en: {extended_zip_path}")