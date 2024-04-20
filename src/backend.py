

import pandas as pd

from contrato import Vendas


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

        return True, errors
    
    except Exception as e:
        return pd.DataFrame(), f"Erro inesperado: {str(e)}"
