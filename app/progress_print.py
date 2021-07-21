import pyperclip
import random
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import locale


locale.setlocale(locale.LC_ALL, 'ru_RU')


def get_url_inn(inn):
    # inn = input('Введите ИНН: ')
    # inn = 7743273995
    user_agent = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
    user_agents = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9',
        'Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4',
        'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240',
        'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
        'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko']

    url = f'https://www.rusprofile.ru/ajax.php?query={inn}&action=search'
    user_agent = {'user-agent': random.choice(user_agents)}
    r = requests.get(url, headers=user_agent).text
    try:
        id_item = r.split(',')[4].split('/')[2].split('"')[0]  # получаем ID
        return f'https://www.rusprofile.ru/id/{id_item}'
    except:
        print('Не могу получить ID')
        print('Приходит в ответе: ', r)


def get_html(url):
    r = requests.get(url)
    if r.ok:
        return r.text
    print(r.status_code)


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    company_name = soup.find('h1').text.strip()
    gen_dir = soup.find('span', class_='company-info__text').text.strip()
    inn = soup.find('span', id="clip_inn").text.strip() ###############
    kpp = soup.find('span', id="clip_kpp").text.strip()
    ogrn = soup.find('span', id='clip_ogrn').text.strip()
    okpo = soup.find('span', id='clip_okpo').text.strip()
    okato = soup.find('span', id='clip_okato').text.strip()
    oktmo = soup.find('span', id='clip_oktmo').text.strip()
    okfs = soup.find('span', id='clip_okfs').text.strip()
    okgu = soup.find('span', id='clip_okogu').text.strip()
    okopf = soup.find('span', id='clip_okopf').text.strip()

    data = {
        'company_name': company_name,
        'gen_dir': gen_dir,
        'inn': inn,
        'kpp': kpp,
        'ogrn': ogrn,
        'okpo': okpo,
        'okato': okato,
        'oktmo': oktmo,
        'okfs': okfs,
        'okgu': okgu,
        'okopf': okopf,
    }
    return data


def mail_generator(string):
    string = string.lower()
    list = string.split()[0:2]
    for i, word in enumerate(list):
        # print(i, word)
        num = random.randint(3, len(word))
        list[i] = word[0:num]
    sep_list = ['', '.', '-']
    sep = random.choice(sep_list)
    string = sep.join(list)
    slovar = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo',
              'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
              'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h',
              'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ъ': 'j', 'ы': 'y', 'ь': 'i', 'э': 'e',
              'ю': 'u', 'я': 'ya'}
    mail_server_list = ['gmail.com', 'yandex.ru', 'outlook.com', 'mail.ru', 'rambler.ru', 'list.ru', 'bk.ru']
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    num1 = random.choice(num_list)
    num2 = random.choice(num_list)
    server = random.choice(mail_server_list)
    for key in slovar:
        string = string.replace(key, slovar[key])
    mail = f'{string}{num1}{num2}@{server}'
    return mail


def get_date():
    pass


def random_name():
    name_list = ['Александр', 'Алексей', 'Анатолий', 'Андрей', 'Антон', 'Аркадий', 'Артем', 'Борислав', 'Вадим',
                 'Валентин', 'Валерий', 'Василий', 'Виктор', 'Виталий', 'Владимир', 'Вячеслав', 'Геннадий', 'Георгий',
                 'Григорий', 'Даниил', 'Денис', 'Дмитpий', 'Евгений', 'Егор', 'Иван', 'Игорь', 'Илья', 'Кирилл', 'Лев',
                 'Максим', 'Михаил', 'Никита', 'Николай', 'Олег', 'Семен', 'Сергей', 'Станислав', 'Степан', 'Федор',
                 'Юрий']
    famely_list = ['Абрамов', 'Александров', 'Алексеев', 'Андреев', 'Антонов', 'Афанасьев', 'Баранов', 'Белов',
                   'Беляев', 'Богданов', 'Борисов', 'Быков', 'Васильев', 'Виноградов', 'Власов', 'Волков', 'Воробьев',
                   'Воронин', 'Гаврилов', 'Герасимов', 'Голубев', 'Григорьев', 'Гусев', 'Давыдов', 'Данилов', 'Денисов',
                   'Дмитриев', 'Егоров', 'Ефимов', 'Жуков', 'Зайцев', 'Захаров', 'Иванов', 'Ильин', 'Исаев', 'Казаков',
                   'Калинин', 'Карпов', 'Киселев', 'Климов', 'Ковалев', 'Козлов', 'Комаров', 'Коновалов', 'Королев',
                   'Крылов', 'Кудрявцев', 'Кузнецов', 'Кузьмин', 'Куликов', 'Лазарев', 'Лебедев', 'Макаров', 'Максимов',
                   'Марков', 'Мартынов', 'Маслов', 'Матвеев', 'Медведев', 'Мельников', 'Миронов', 'Михайлов', 'Морозов',
                   'Назаров', 'Никитин', 'Николаев', 'Новиков', 'Орлов', 'Осипов', 'Павлов', 'Петров', 'Поляков',
                   'Пономарев', 'Попов', 'Родионов', 'Романов', 'Савельев', 'Семенов', 'Сергеев', 'Сидоров', 'Смирнов',
                   'Соколов', 'Соловьев', 'Сорокин', 'Степанов', 'Тарасов', 'Тимофеев', 'Титов', 'Тихонов', 'Федоров',
                   'Федотов', 'Филатов', 'Филиппов', 'Фомин', 'Фролов', 'Чернов', 'Чернышев', 'Щербаков', 'Яковлев']
    full_name = random.choice(famely_list) + ' ' + random.choice(name_list)
    return full_name


def mail_assembly(data):
    ot_kogo_name = random_name()
    ot_kogo_mail = mail_generator(ot_kogo_name)
    now = datetime.now()
    date = f"{now.strftime('%A, %d %b %Y, %H:%M')} +03:00"
    tema = 'ООО СМАРТСЕРВИС'

    company_name = data['company_name']
    gen_dir = data['gen_dir']
    inn = data['inn']
    kpp = data['kpp']
    ogrn = data['ogrn']
    okpo = data['okpo']
    okato = data['okato']
    oktmo = data['oktmo']
    okfs = data['okfs']
    okgu = data['okgu']
    okopf = data['okopf']

    ogrn = '1203500002870'

    res = f'-------- Пересылаемое сообщение --------\nОт кого: {ot_kogo_name} <{ot_kogo_mail}>\n' \
          f'Дата: {date}\n' \
          f'Тема: {company_name}\n\n' \
          f'ГЕНЕРАЛЬНЫЙ ДИРЕКТОР: {gen_dir}\n' \
          f'{company_name}\n' \
          f'ИНН {inn}\n' \
          f'ОГРН {ogrn}\n============================================\n\n' \
          f'ИНН {inn}    КПП {kpp}             ОГРН  {ogrn}\n\n' \
          f'ОКПО {okpo}     ОКАТО {okato}     ОКТМО {oktmo}\n\n' \
          f'ОКФС {okfs}                ОКОГУ {okgu}            ОКОПФ {okopf}\n'

    # pyperclip.copy(res)
    # print(res)
    return res


def main(search_str):
    # inn = input('Поисковый запрос: ')
    # inn = 5507228812
    url = get_url_inn(search_str)
    if url is None:
        return 'Ничего не могу найти!\nуточните поисковый запрос..'
    data = get_data(get_html(url))
    res = mail_assembly(data) ##########
    print(res)
    pyperclip.copy(res)
    return res
    # print(data)


if __name__ == '__main__':
    search_str = '5507228812'
    main(search_str)

