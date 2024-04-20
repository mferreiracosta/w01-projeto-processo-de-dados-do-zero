import subprocess
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    # Iniciar o Streamlit em background
    process = subprocess.Popen(["streamlit", "run", "src/app.py"])
    options = Options()
    options.headless = True  # Executar em modo headless
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(5)
    yield driver

    # Fechar o browser e o Streamlit após o teste
    driver.quit()
    process.kill()

def test_app_opens(driver):
    # Verificar se a página abre
    driver.get("http://localhost:8501")
    sleep(5)

def test_check_title_is(driver):
    # Verificar se a página abre
    driver.get("http://localhost:8501")
    sleep(2)

    page_title = driver.title  # Obter o título da página

    # Verificar se o título da página é o esperado
    expected_title = "Validador de schema excel"
    assert page_title == expected_title

def test_check_streamlit_h1(driver):
    # Verificar se a página abre
    driver.get("http://localhost:8501")
    sleep(2)

    # Capturar o elemento <h1> da página
    h1_element = driver.find_element(By.TAG_NAME, "h1")

    # Verificar se o texto do elemento <h1> é o esperado
    expected_text = "Insira o excel para validação"
    assert h1_element.text == expected_text
