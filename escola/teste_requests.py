import requests


# GET Avaliacoes
headers = {
    'content-type': 'application/json',
    'Authorization': 'Token 80ca9f249b80e7226cdc7fcaada8d7297352f0f9'
}
avaliacoes = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/', headers=headers)

#print(avaliacoes.status_code)

# print(avaliacoes.json())

# print(avaliacoes.json()['count'])

# print(avaliacoes.json()['next'])

# print(avaliacoes.json()['results'])

# GET Avaliacoes id
headers = {
    'content-type': 'application/json',
    'Authorization': 'Token 80ca9f249b80e7226cdc7fcaada8d7297352f0f9'
}
avaliacoes = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/2/', headers=headers)


# print(avaliacoes.json())

# GET Cursos
headers = {
    'content-type': 'application/json',
    'Authorization': 'Token 80ca9f249b80e7226cdc7fcaada8d7297352f0f9'
}
cursos = requests.get('http://127.0.0.1:8000/api/v2/cursos/', headers=headers)

# print(cursos.json())