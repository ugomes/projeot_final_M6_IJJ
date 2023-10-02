from behave import given, when, then
from behave import fixture, use_fixture
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep


url = "https://projetofinal.jogajuntoinstituto.org/"


@fixture
def setup_navegador(context):
    context.navegador = Firefox()
    context.navegador.maximize_window()
    context.navegador.get(url)

def before_all(context):
 
           
        use_fixture(setup_navegador, context)

       
        name_email = context.navegador.find_element(By.NAME, "email")
        name_email.send_keys("teste123@teste.com.br")
        name_password = context.navegador.find_element(By.NAME, "password")
        name_password.send_keys("123@mudar")
        button_iniciar_sessao = context.navegador.find_element(By.CLASS_NAME, 'sc-eqUAAy')
        button_iniciar_sessao.click()

        sleep(1)

        botao_perfil = context.navegador.find_element(By.ID, "radix-7-trigger-radix-0")
        texto_botao = botao_perfil.text
        sleep(3)
        assert texto_botao == "Perfil"

def after_all(context): 
    sleep(3)
    context.navegador.quit()       
    