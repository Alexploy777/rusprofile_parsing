import requests
import fake_useragent
from bs4 import BeautifulSoup
import re



class Parser:
    prefix_id_client = ''  # рабочие варианты ip, id
    id_client = ''
    url_client = ''
    url_clien_requisites = ''
    def __init__(self, search_str):
        self.url = f'https://www.rusprofile.ru/ajax.php?query={search_str}&action=search'
        self.get_id_client()

    def get_id_client(self):
        user_agent = {'user-agent': fake_useragent.UserAgent().random}  # Берем случайный user_agent
        print(user_agent) # ПОТОМ УБРАТЬ!
        r_id_item = requests.get(self.url, headers=user_agent).json()  # принимаем json ответа
        # у разных запросов нужные данные могут оказаться под разными ключами, поэтому:
        try:
            if 'ip' in r_id_item:  # если ключ 'ip' в ответе (json)
                link = r_id_item['ip'][0]['link']
            elif 'ul' in r_id_item:  # если ключ 'ul'
                link = r_id_item['ul'][0]['link']
            else:
                link = '/search_inactive=0'  # исключение

            # print(link) # ПОТОМ УБРАТЬ!

            if link == '/search_inactive=0':
                Parser.prefix_id_client = None
                Parser.id_client = None
            else:
                Parser.prefix_id_client = link[1:3]
                Parser.id_client = link[4::]

            # dic_id_client = {prefix_id_client : id_client}
            # print(dic_id_client) # ПОТОМ УБРАТЬ!
            # return dic_id_client

            # if flag == 'ofd':
            #     url_client = 'https://www.rusprofile.ru' + '/requisites' + link[3::]  # получили прямую ссылку на реквизиты клиента https://www.rusprofile.ru/requisites/11556591
            # else:
            #     url_client = 'https://www.rusprofile.ru' + link  # получили прямую ссылку на клиента https://www.rusprofile.ru/id/11556591
            # # print(url_client)
            # return url_client  # вернули ссылку на клиента
        except:
            print('Не могу получить ID')
            print('Приходит в ответе: ', r_id_item)

    def get_ofd_data(self):
        kpp = None
        fns = None
        pfr = None
        okpo = None
        fss = None
        fio = None

        if Parser.prefix_id_client == 'id':  # клиенты, где в адресе ID
            Parser.url_client = 'https://www.rusprofile.ru/' + 'id/' + Parser.id_client
            Parser.url_clien_requisites = 'https://www.rusprofile.ru' + '/requisites/' + Parser.id_client

            requisites = requests.get(Parser.url_clien_requisites).text  # запрос страницы реквизитов

            kpp = re.findall(r'(?<=<span\ class="copy-value"\ id="clip_kpp">).*?(?=</span>)', requisites)[0]
            fns = kpp[0:4]
            pfr = re.findall(r'(?<=<span\ class="copy-value"\ id="clip_pfr_num">).*?(?=</span>)', requisites)[0]
            # kpp = re.findall(r'(?<=<span\ class="copy-value"\ id="clip_kpp">).*?(?=</span>)', requisites)[0]
            okpo = re.findall(r'(?<=<span\ class="copy-value"\ id="clip_okpo">).*?(?=</span>)', requisites)[0]
            fss = re.findall(r'(?<=<span\ class="copy-value"\ id="clip_fss_num">).*?(?=</span>)', requisites)[0]

            home = requests.get(Parser.url_client).text  # запрос главной страницы
            home_soup = BeautifulSoup(home, 'lxml')
            fio = home_soup.find('div', class_='company-row hidden-parent').find('span', class_='company-info__text').text.strip()


        elif Parser.prefix_id_client == 'ip':  # клиенты, где в адресе IP
            Parser.url_client = 'https://www.rusprofile.ru' + '/ip/' + Parser.id_client

            requisites = requests.get(Parser.url_client).text
            pfr = re.findall(r'(?<=<span\ class="copy_target"\ id="req_pfr">).*?(?=</span>)', requisites)[0]
            okpo = re.findall(r'(?<=<span\ class="copy_target"\ id="req_okpo">).*?(?=</span>)', requisites)[0]
            fss = re.findall(r'(?<=<span\ class="copy_target"\ id="req_fss">).*?(?=</span>)', requisites)[0]
            fio = re.findall(r'(?<=\ <h2\ class="company-name">)[\w\W]*?(?=</h2>)', requisites)[0].strip()

        else:
            print('некорректный запрос или надо вводить капчу!')

        data = {
            'фио': fio,
            'фнс': fns,
            'пфр': pfr,
            'росстат': okpo,
            'фсс': fss,
        }
        print(data)
        return data

        # print(Parser.url_client)
        # print(Parser.url_clien_requisites)
        # print('fns =', fns, 'pfr =', pfr, 'kpp =', kpp, 'okpo =', okpo, 'fss =', fss, 'fio =', fio )


def main(search_str):
    client = Parser(search_str) # создали объект класса Parser
    # dic_id_client = client.get_id_client() # получили id клиента и префикс этого id
    # data_client = client.get_data_client()


    # print(client.prefix_id_client, client.id_client) # ПОТОМ УБРАТЬ!
    ofd = client.get_ofd_data()
    # print(client.url_client, client.url_clien_requisites)

if __name__ == '__main__':
    search_str = '7743273995'
    search_str = '7743273995'
    search_str = '9710072366'
    # search_str = '6021000115'
    search_str = '319508100007136'
    # search_str = 'ывапыв'
    main(search_str)
'''
1.  Нужно получать только id клиента и только его отправлять в дальнейшие методы
2.  Сделать метод "получить суп", параметр - реквизиты, главная и т.д.
3.  суп - параметр get_data_client и далее запрашиваем тот или иной суп и парсим данные 
'''