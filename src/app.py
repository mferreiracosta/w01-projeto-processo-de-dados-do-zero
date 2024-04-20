import logging

import sentry_sdk

from backend import load_excel_to_database, process_excel
from frontend import ExcelValidatorUI

sentry_sdk.init(
    dsn="https://f6e11a97aead4f6f20d6788da4b60d12@o4507120429170688.ingest.us.sentry.io/4507120472424448",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

def main():
    ui = ExcelValidatorUI()
    ui.display_header()

    upload_file = ui.upload_file()
    if upload_file:
        df, result, errors = process_excel(upload_file)
        ui.display_results(result, errors)

        if errors:
            ui.display_error_message()
            logging.error("Planilha com erro de schema")
            sentry_sdk.capture_message("Planilha com erro de schema (Mensagem Sentry)")
        elif ui.display_save_button():
            load_excel_to_database(df)
            ui.display_success_message()
            logging.info("Banco de dados SQL atualizado")
            sentry_sdk.capture_message("Banco de dados SQL atualizado (Mensagem Sentry)")


if __name__ == "__main__":
    main()