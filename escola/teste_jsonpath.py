import requests
import jsonpath

# GET Avaliacoes
headers = {
    'content-type': 'application/json',
    'Authorization': 'Token 80ca9f249b80e7226cdc7fcaada8d7297352f0f9'
}
avaliacoes = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/', headers=headers)

# resultados = jsonpath.jsonpath(avaliacoes.json(), 'results')

# print(resultados)

# primeira = jsonpath.jsonpath(avaliacoes.json(), 'results[0]')

# print(primeira)

# primeira = jsonpath.jsonpath(avaliacoes.json(), 'results[0].nome')

# print(primeira)

# primeira = jsonpath.jsonpath(avaliacoes.json(), 'results[*].nome')

# print(primeira)