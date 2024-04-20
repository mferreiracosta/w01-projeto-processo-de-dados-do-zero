from backend import process_excel
from frontend import ExcelValidatorUI


def main():
    ui = ExcelValidatorUI()
    ui.display_header()

    upload_file = ui.upload_file()
    if upload_file:
        result, errors = process_excel(upload_file)
        ui.display_results(result, errors)


if __name__ == "__main__":
    main()