import re
import json


def get_words_list():
    words = open('utils/words_bank.txt', 'r')

    words_list = [re.match(r'\S+', line).group() for line in words.readlines()]

    return words_list


def get_data():
    with open('db.json', encoding="utf8") as data_file:
        data = json.load(data_file)
    return data
