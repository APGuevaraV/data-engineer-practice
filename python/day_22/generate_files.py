import os
import shutil
import random
from datetime import datetime, timedelta


if os.path.exists('reportes'):
    shutil.rmtree('reportes')

if os.path.exists('reportes_organizados'):
    shutil.rmtree('reportes_organizados')


OUTPUT_DIR = 'reportes'
os.makedirs(OUTPUT_DIR, exist_ok=True)


def random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)


start_date = datetime.today() - timedelta(days=30)
end_date = datetime.today()

sources = [
    ("ventas", ".csv"),
    ("clientes", ".csv"),
    ("productos", ".json"),
]

for source, extension in sources:
    num_files = random.randint(2, 4)

    for _ in range(num_files):
        date_str = random_date(start_date, end_date).strftime("%Y-%m-%d")
        filename = f"{source}_{date_str}{extension}"
        filepath = os.path.join(OUTPUT_DIR, filename)
        open(filepath, 'a').close()
        print(f"==> Archivo creado: {filepath}")
