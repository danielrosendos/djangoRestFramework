import requests

headers = {
    'content-type': 'application/json',
    'Authorization': 'Token 80ca9f249b80e7226cdc7fcaada8d7297352f0f9'
}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes'

resultado = requests.get(url=url_base_cursos, headers=headers)

assert resultado.status_code == 200