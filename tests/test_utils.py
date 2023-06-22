from src.utils import load_data,executed_operations,last_operations,account_mask,card_mask,date
import json
def test_load_data():
    test_file = [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }
]
    assert load_data("src/test_file.json") == test_file

def test_executed_operations():
    assert executed_operations([{"state": "EXECUTED"}]) == [{"state": "EXECUTED"}]

def test_last_operations():
    assert last_operations([{"date": "2019-01-05T00:52:30.108534"}]) == [{"date": "2019-01-05T00:52:30.108534"}]

def test_account_mask():
    assert account_mask("Счет 46363668439560358409") == "Счет ** 8409"

def test_card_mask():
    assert card_mask("Maestro 7810846596785568") == "Maestro 7810 84** **** 5568"
    assert card_mask("Visa Gold 3654412434951162") == "Visa Gold 3654 41** **** 1162"

def test_date():
    assert date("2018-06-20T03:59:34.851630") == "20.06.2018"

