from httpx import get
import fire
from parsel import Selector


def dollar():
    response = get('https://economia.awesomeapi.com.br/all/USD').json
    return response


def tv(canal):
    response = get(f'https://meuguia.tv/programacao/canal/{canal}').text
    s = Selector(response)
    return {
        'Nome': s.css('h2::text').get(),
        'Horário':s.css('div.time::text').get(),
        'Tipo': s.css('h3::text').get()

    }


def cep(num):
    response = get(f'https://cep.awesomeapi.com.br/json/{num}').json
    return response


class Jogos:
    def megasena(self):
        response = get('https://lotericas.io/api/v1/jogos/megasena/lasted').json()
        return response['data'][0]['listaDezenas']


fire.Fire()
