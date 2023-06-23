import json
"""Импорт библиотеки для работы с json файлами"""

filepath = 'operations.json'

def load_data(filepath):
    """
    Загрузка исходных данных
    """
    with open(filepath, 'r',encoding='utf-8') as file:
        data = json.load(file)
        return data

def executed_operations(data):
    """
    Получение исполненных операций
    """
    state = []
    for i in data:
        if i.get('state') == 'EXECUTED':
            state.append(i)
    return state

def last_operations(data):
    """
    Выбор пяти последних операций
    """
    data.sort(key=lambda x: x.get('date'))
    data.reverse()
    return data[:5]

def account_mask(data):
    """
    Маскировка данных счета
    """
    account_list = data.split(" ")
    numb = account_list[-1]
    return account_list[0] + " " + "**" + " " + numb[-4:]

def card_mask(data):
    """
    Маскировка данных карты
    """
    account_list = data.split(" ")
    if len(account_list) > 2:
        numb = account_list[-1]
        return account_list[0] + " " + account_list[1] + " " + numb[0:4] + " " + numb[4:6] + "** ****" + " " + numb[-4:]
    else:
        account_list = data.split(" ")
        numb = account_list[-1]
        return account_list[0] + " " + numb[0:4] + " " + numb[4:6] + "** ****" + " " + numb[-4:]

def date(date_str):
    """
    Преобразование даты
    """
    date_str = date_str[:10].split('-')
    new_date_str = date_str[2] + "." + date_str[1] + "." + date_str[0]
    return new_date_str
