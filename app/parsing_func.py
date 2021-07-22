import requests
import fake_useragent
from bs4 import BeautifulSoup


class Parser:
    def __init__(self, search_str):
        self.url = f'https://www.rusprofile.ru/ajax.php?query={search_str}&action=search'

    def get_url_client(self):
        user_agent = {'user-agent': fake_useragent.UserAgent().random}  # Берем случайный user_agent
        r_id_item = requests.get(self.url, headers=user_agent).json()  # принимаем json ответа
        # у разных запросов нужные данные могут оказаться под разными ключами, поэтому:
        if 'ip' in r_id_item:  # если ключ 'ip'
            link = r_id_item['ip'][0]['link']
        elif 'ul' in r_id_item:  # если ключ 'ul'
            link = r_id_item['ul'][0]['link']
        else:
            link = 'oops'  # исключение

        url_client = 'https://www.rusprofile.ru' + link  # получили прямую ссылку на клиента
        return url_client # вернули ссылку на клиента
        # print(url_client)


def main(search_str):
    client = Parser(search_str)
    link = client.get_url_client()
    print(link)


if __name__ == '__main__':
    search_str = '7743273995'
    main(search_str)
