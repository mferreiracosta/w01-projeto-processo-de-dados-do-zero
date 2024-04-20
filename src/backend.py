import os

import pandas as pd
from dotenv import load_dotenv

from contrato import Vendas

load_dotenv(".env")

# Lendo as variáveis de ambiente
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")

# Cria a URL de conexão com o banco de dados
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"


def process_excel(uploaded_file):
    try:
        df = pd.read_excel(uploaded_file)
        errors = []

        # Verificar se existe colunas extras vindo do Excel
        extra_cols = set(df.columns) - set(Vendas.model_fields.keys())
        if extra_cols:
            errors.append(f"Colunas que não fazem parte do schema no contrato: {', '.join(extra_cols)}")
            return False, errors

        # Validar cada linha com o schema implementado
        for index, row in df.iterrows():
            try:
                _ = Vendas(**row.to_dict())
            except Exception as e:
                errors.append(f"Erro na linha {index + 2}: {e}")

        return df, True, errors
    
    except Exception as e:
        return pd.DataFrame(), f"Erro inesperado: {str(e)}"

def load_excel_to_database(df: pd.DataFrame):
    df.to_sql(name="vendas", con=DATABASE_URL, if_exists="replace", index=False)
