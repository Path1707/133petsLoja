import pytest
import requests

base_url = 'https://petstore.swagger.io/v2'
headers = {'Content-Type': 'application/json'}


def testar_incluir_usuario():
    # Configura
    # Dados de entrada: virão do pet1.json
    # Resultado Esperado
    status_code_esperado = 200
    code_esperado = 200
    type_esperado = 'unknown'
    message_esperado = '12154651'

    # Executa
    resultado_obtido = requests.post(url=base_url + '/user',
                                     data=open('C:\\Users\\pathm\\PycharmProjects\\133pets\\vendors\\json\\user1.json',
                                               'rb'),
                                     headers=headers
                                     )

    # Valida
    print(resultado_obtido)
    corpo_da_resposta = resultado_obtido.json()
    print(corpo_da_resposta)
    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == code_esperado
    assert corpo_da_resposta['type'] == type_esperado
    assert corpo_da_resposta['message'] == message_esperado

def testar_consultar_user():
    # 1 - Configura
    # 1.1 Dados de entrada
    user_username = 'pathcarvalho'
    # 1.2 Resultados Esperados

    status_code_esperado = 200
    nome_user_esperado = 'Patricia'
    sobrenome_user_esperado = 'Carvalho'
    email_user_esperado = 'path.monteiro17@gmail.com'

    # Executa
    resultado_obtido = requests.get(
        url=base_url + '/user/' + user_username,  # https://petstore.swagger.io/v2/user/pathcarvalho
        headers=headers
    )

    # Valida
    print(resultado_obtido)
    corpo_da_resposta = resultado_obtido.json()
    print(corpo_da_resposta)
    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_da_resposta['firstName'] == nome_user_esperado
    assert corpo_da_resposta['lastName'] == sobrenome_user_esperado
    assert corpo_da_resposta['email'] == email_user_esperado

def testar_alterar_user():
    user_username = 'pathcarvalho'
    status_code_esperado = 200
    code_esperado = 200
    type_esperado = 'unknown'
    message_esperado = '12154651'

    resultado_obtido = requests.put(
        url=f'{base_url}/user/{user_username}',
        data=open('C:\\Users\\pathm\\PycharmProjects\\133pets\\vendors\\json\\user2.json', 'rb'),
        headers=headers
    )

    corpo_da_resposta = resultado_obtido.json()
    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == code_esperado
    assert corpo_da_resposta['type'] == type_esperado
    assert corpo_da_resposta['message'] == message_esperado

def testar_excluir_user():
    user_username = 'pathcarvalho'

    status_code_esperado = 200
    code_esperado = 200
    type_esperado = 'unknown'
    message_esperado = user_username

    resultado_obtido = requests.delete(
        url='https://petstore.swagger.io/v2/user/pathcarvalho',
        headers=headers
    )

    corpo_da_resposta = resultado_obtido.json()
    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == code_esperado
    assert corpo_da_resposta['type'] == type_esperado
    assert corpo_da_resposta['message'] == message_esperado






