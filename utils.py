import json

filepath = 'operations.json'

def load_data(filepath):
    with open(filepath, 'r',encoding='utf-8') as file:
        data = json.load(file)

def executed_operations(data):
    state = []
    for i in data:
        if i.get('state') == 'EXECUTED':
            state.append(i)
    return state

def last_operations(data):
    data.sort(key=lambda x: x.get)