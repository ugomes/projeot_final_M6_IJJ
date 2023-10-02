#language: pt

Funcionalidade: Cadastro produto

    Como vendedor da loja
    Quero cadastrar um produto
    Para que possa ser vendido no site

    # Pré-condição: Ter um conta criada para fazer o login
    
Cenário: Cadastro de um produto na loja
    Quando clico em adicionar 
    E preencho o campo Nome do Produto
    E descricao do produto
    E seleciono a categoria Roupa
    E preencho o campo preco
    E seleciono uma imagem
    E preencho o valor do frete
    E clico em enviar novo produto
    Então o alerta produto enviado com sucesso aparece
    