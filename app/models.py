from utils.read import *
from utils.write import *
from utils.tokenizer_words import *
from collections import OrderedDict


def filter_words(contents):
    words_list = get_words_list()
    words = get_tokenized_words(contents)
    new_words = [word.lower() for word in words if word.lower() not in words_list]
    new_words = list(OrderedDict.fromkeys(new_words))
    new_words.sort()
    return new_words


def get_article():
    data = get_data()
    return data['article'][0]['contents']


def get_new_words():
    data = get_data()
    return data['article'][1]['newWords']


def add_words(words):
    add_to_words_bank(words)


def write_db(data):
    write_to_db(data)

