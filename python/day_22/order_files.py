import os
import shutil


SOURCES = ['ventas', 'clientes', 'productos']
INPUT_DIR = 'reportes'
OUTPUT_DIR = 'reportes_organizados'
os.makedirs(OUTPUT_DIR, exist_ok=True)

for source in SOURCES:
    ruta = os.path.join(OUTPUT_DIR, source)
    os.makedirs(ruta, exist_ok=True)


for filename in os.listdir(INPUT_DIR):
    filepath = os.path.join(INPUT_DIR, filename)
    print(filepath)

    if not os.path.isfile(filepath):
        continue

    if '_' not in filename:
        continue

    source = filename.split('_')[0].lower()

    if source in SOURCES:
        print(source)
        target_dir = os.path.join(OUTPUT_DIR, source)
        target_path = os.path.join(target_dir, filename)
        shutil.move(filepath, target_path)
        print(f"==> Moviendo: {filename} -> {target_dir}")
    else:
        print('Archivo no considerado para el ordenamiento')
