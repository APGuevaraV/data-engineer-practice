
# Removing folders if it exists
from sqlalchemy import create_engine
import pandas as pd
import os
import shutil

file_path = os.path.join('.', 'server_inputs', 'file.ope')
file_cliente = os.path.join('.', 'server_outputs', 'cliente.csv')
file_deuda = os.path.join('.', 'server_outputs', 'deuda.csv')

tabla_cliente = 'tbl_cliente'
tabla_deuda = 'tbl_deuda'


def setup():
    folders = ['database', 'server_inputs', 'server_outputs']

    for folder in folders:
        if os.path.exists(folder):
            shutil.rmtree(folder)

    # Generando archivos iniciales

    os.mkdir('database')
    os.mkdir('server_inputs')
    os.mkdir('server_outputs')

    git_path = 'https://raw.githubusercontent.com/AngelTintaya/datasets/refs/heads/main/file.ope'

    pd.read_csv(git_path).to_csv(file_path, index=False)
