import requests

def exemplo_cep():
    cep = "16705332"
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response_cep = requests.get(url)

    if response_cep.status_code == 200:
        dados_cep = response_cep.json()
        print(f' Rua: {dados_cep["logradouro"]}')
        print(f' Bairro: {dados_cep["bairro"]}')
        print(f' Localidade: {dados_cep["localidade"]}')
        print(f' Região: {dados_cep["regiao"]}')

    else:
        print(f' Erro: {response_cep.status_code}')

def exemplo_get(id):
    url = f'https://jsonplaceholder.typicode.com/posts/{id}'
    response_get = requests.get(url)
    if response_get.status_code == 200:
        dados_get = response_get.json()
        print(f' Titulo: {dados_get["title"]}')
        print(f' Conteudo: {dados_get["body"]}')
    else:
        print(f' Erro: {response_get.status_code}')


def exemplo_post():
    url = 'https://jsonplaceholder.typicode.com/posts'

    nova_postagem = {
        "title": "Novo titulo",
        "body": "Novo conteudo",
        "userId": 1
    }

    response = requests.post(url, json=nova_postagem)

    if response.status_code == 201:
        dados_post = response.json()
        print(f' Titulo: {dados_post["title"]}')
        print(f' Conteudo: {dados_post["body"]}\n')
    else:
        print(f' Erro: {response.status_code}')

    response_post = requests.post(url)
def exemplo_put(id, id_usuario):
    url = f'https://jsonplaceholder.typicode.com/posts/{id}'

    nova_postagem = {
        "id": id,
        "title": "Novo titulo",
        "body": "Novo conteudo",
        "userId": id_usuario
    }

    antes = requests.get(url)
    response = requests.put(url, json=nova_postagem)

    if response.status_code == 200:
        if antes.status_code == 200:
            dados_antes = antes.json()
            print(f' Titulo antigo: {dados_antes["title"]}')
        else:
            print(f' Erro: {response.status_code}')
        dados_put = response.json()
        print(f' Titulo: {dados_put["title"]}')
        print(f' Conteudo: {dados_put["body"]}\n')
    else:
        print(f' Erro: {response.status_code}')

# exemplo_get(50)
# exemplo_post()
exemplo_put(40, 1)
