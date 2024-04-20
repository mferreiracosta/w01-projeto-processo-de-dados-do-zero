import streamlit as st


class ExcelValidatorUI:

    def __init__(self):
        self.set_page_config()

    def set_page_config(self):
        st.set_page_config(
            page_title="Validador de schema excel"
        )

    def display_header(self):
        st.title("Insira o excel para validação")

    def upload_file(self):
        return st.file_uploader("Carregue seu arquivo excel aqui", type=["xlsx"])
    
    def display_results(self, result, errors):
        if errors:
            for error in errors:
                st.error(f"Erro na validação: {error}")
        else:
            st.success("O schema do arquivo excel está correto!")

    def display_save_button(self):
        return st.button("Salvar no Banco de Dados")
    
    def display_error_message(self):
        return st.error("Necessário corrigir a planilha!")
    
    def display_success_message(self):
        return st.success("Dados salvos com sucesso no banco de dados!")
