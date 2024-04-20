from backend import process_excel, load_excel_to_database
from frontend import ExcelValidatorUI


def main():
    ui = ExcelValidatorUI()
    ui.display_header()

    upload_file = ui.upload_file()
    if upload_file:
        df, result, errors = process_excel(upload_file)
        ui.display_results(result, errors)

        if errors:
            ui.display_error_message()
        elif ui.display_save_button():
            load_excel_to_database(df)
            ui.display_success_message()


if __name__ == "__main__":
    main()