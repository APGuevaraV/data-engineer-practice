
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


def extract(file):
    # EXTRACT
    df = pd.read_csv(file)
    df['Type'] = df['Field_1'].astype('str').str[0]
    df_cliente = df[df['Type'] == '1'].reset_index(drop=True).copy()
    df_deuda = df[df['Type'] == '2'].reset_index(drop=True).copy()
    return df_cliente, df_deuda


def transform(df_cliente_raw, df_deuda_raw):
    # Transform
    # Cliente
    df_cliente_clean = df_cliente_raw['Field_1'].astype(
        'str').str[1:].str.split('|', expand=True)
    df_cliente_clean.head()

    headers_cliente = {
        0: 'SBSCodigoCliente',
        1: 'SBSFechaReporte',
        2: 'SBSTipoDocumentoT',
        3: 'SBSRucCliente',
        4: 'SBSTipoDocumento',
        5: 'SBSNumeroDocumento',
        6: 'SBSTipoPer',
        7: 'SBSTipoEmpresa',
        8: 'SBSNumeroEntidad',
        9: 'SBSSalNor',
        10: 'SBSSalCPP',
        11: 'SBSSalDEF',
        12: 'SBSSalDUD',
        13: 'SBSSalAPER',
        14: 'SBSAPEPAT',
        15: 'SBSAPEMAT',
        16: 'SBSAPECAS',
        17: 'SBSNOMCLI',
        18: 'SBSNOMCLI2'
    }

    df_cliente_clean.rename(columns=headers_cliente, inplace=True)

    # deuda
    df_deuda_raw['CodigoSBS'] = df_deuda_raw['Field_1'].astype('str').str[1:11]
    df_deuda_raw['CodigoEmpresa'] = df_deuda_raw['Field_1'].astype(
        'str').str[11:16]
    df_deuda_raw['TipoCredito'] = df_deuda_raw['Field_1'].astype(
        'str').str[16:18]
    df_deuda_raw['Nivel2'] = df_deuda_raw['Field_1'].astype('str').str[18:20]
    df_deuda_raw['Moneda'] = df_deuda_raw['Field_1'].astype('str').str[20]
    df_deuda_raw['SubCodigoCuenta'] = df_deuda_raw['Field_1'].astype(
        'str').str[21:32]
    df_deuda_raw['Condicion'] = df_deuda_raw['Field_1'].astype(
        'str').str[32:38]
    df_deuda_raw['ValorSaldo'] = df_deuda_raw['Field_1'].astype(
        'str').str[38:42]
    df_deuda_raw['ClasificacionDeuda'] = df_deuda_raw['Field_1'].astype(
        'str').str[42]
    df_deuda_raw['CodigoCuenta'] = df_deuda_raw['Nivel2'] + \
        df_deuda_raw['Moneda']+df_deuda_raw['SubCodigoCuenta']

    headers_deuda = {
        'CodigoSBS': 'Cod_SBS',
        'CodigoEmpresa': 'Cod_Emp',
        'TipoCredito': 'Tip_Credit',
        'ValorSaldo': 'Val_Saldo',
        'ClasificacionDeuda': 'Clasif_Deu',
        'CodigoCuenta': 'Cod_Cuenta'

    }

    df_deuda_raw.rename(columns=headers_deuda, inplace=True)
    df_deuda_raw.drop(columns=['Field_1', 'Type'], inplace=True)

    return df_cliente_clean, df_deuda_raw
