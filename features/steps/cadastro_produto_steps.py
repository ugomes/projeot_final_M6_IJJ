from behave import given, when, then
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep




@when('clico em adicionar')
def clicar_adicionar(context):

    botao_adicionar = context.navegador.find_element(By.CSS_SELECTOR, "button[type='button'][aria-haspopup='dialog'][aria-expanded='false'][aria-controls='radix-6']")
    botao_adicionar.click()

@when('preencho o campo Nome do Produto')
def step_preencher_nome_produto(context):
    nome_do_produto = context.navegador.find_element(By.NAME,"name")
    nome_do_produto.click()
    nome_do_produto.send_keys(" Calça Jeans")

@when('descricao do produto')
def step_preencher_descricao(context):
    descricao_produto = context.navegador.find_element(By.NAME,"description")
    descricao_produto.click()
    descricao_produto.send_keys("Calça Jeans da Moda")

@when('seleciono a categoria Roupa')
def step_selecionar_categoria_roupa(context):
    categoria_roupa = context.navegador.find_element(By.XPATH, "//label[span[text()='Roupas']]")
    categoria_roupa.click()



@when('preencho o campo preco')
def step_preencher_preco(context):
    preco = context.navegador.find_element(By.NAME,"price")
    preco.click()
    preco.send_keys("100,01")



@when('seleciono uma imagem')
def step_selecionar_imagem(context):
    upload_imagem = context.navegador.find_element(By.NAME,"image")
    caminho_imagem = "E:\Projeto_Final_IJJ_V.F\imagem\calcajeans.jpeg"
    upload_imagem.send_keys(caminho_imagem)

@when('preencho o valor do frete')
def step_preencher_valor_frete(context):
    frete = context.navegador.find_element(By.NAME, "shipment")
    frete.click()
    frete.send_keys("15,50")

@when('clico em enviar novo produto')
def step_clicar_enviar_produto(context):
    enviar_cadastrado = context.navegador.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    enviar_cadastrado.submit()


@then('o alerta produto enviado com sucesso aparece')

def step_alerta_produto (context):
    sleep(1)
    caminho_salvar_imagem ="E:\Projeto_Final_IJJ_V.F\evidencia"
    context.navegador.save_screenshot(caminho_salvar_imagem)
 
    
    
    




