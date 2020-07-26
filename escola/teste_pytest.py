import requests

class TestCurso:
    headers = {
        'content-type': 'application/json',
        'Authorization': 'Token 80ca9f249b80e7226cdc7fcaada8d7297352f0f9'
    }
    url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'

    def test_get_cursos(self):
        cursos = requests.get(url=self.url_base_cursos, headers=self.headers)

        assert cursos.status_code == 200


    def test_get_curso(self):
         cursos = requests.get(url=f'{self.url_base_cursos}2/', headers=self.headers)

         assert cursos.status_code == 200


    def test_post_curso(self):
        novo = {
            "titulo": "Curso de Ruby",
            "url": "http://testederuby.com.br"
        }

        resultado = requests.post(url=self.url_base_cursos, headers=self.headers, data=novo)

        assert resultado.status_code == 201
        assert resultado.json()['titulo'] == novo['titulo']


    def test_put_curso(self):
        atualizado = {
            "titulo": "Novo Curso de Ruby",
            "url": "http://novocursoderuby.com.br"
        }

        resposta = requests.put(url=f'{self.url_base_cursos}2/', headers=self.headers, data=atualizado)

        assert resposta.status_code == 200


    def test_put_titulo_curso(self):
        atualizado = {
            "titulo": "Novo Curso de Ruby",
            "url": "http://novocursoderuby.com.br"
        }

        resposta = requests.put(url=f'{self.url_base_cursos}2/', headers=self.headers, data=atualizado)

        assert resposta.status_code == 200
        assert resposta.json()['titulo'] == atualizado['titulo']
    

    def test_delete_curso(self):
        resposta = requests.put(url=f'{self.url_base_cursos}2/', headers=self.headers)

        assert resposta.status_code == 204 and len(resposta.text) == 0