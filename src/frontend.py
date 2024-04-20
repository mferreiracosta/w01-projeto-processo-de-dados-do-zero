import streamlit as st


class ExcelValidatorUI:

    def __init__(self):
        self.set_page_config()

    def set_page_config(self):
        st.set_page_config(
            page_title="Validador de schema excel"
        )

    def display_header(self):
        st.title("Não gosto do meu cliente")

    def upload_file(self):
        return st.file_uploader("Carregue seu arquivo excel aqui", type=["xlsx"])
    
    def display_results(self, result, errors):
        if errors:
            for error in errors:
                st.error(f"Erro na validação: {error}")
        else:
            st.success("O schema do arquivo excel está correto!")
