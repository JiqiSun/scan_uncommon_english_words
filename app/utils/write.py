import json


def add_to_words_bank(words):
    with open('utils\\words_bank.txt', 'a') as f:
        for word in words:
            f.write(word+'\n')


def write_to_db(data):
    with open('db.json', 'w', encoding='utf8') as f:
        _str = json.dumps(data, indent=4, sort_keys=True,
                          separators=(',', ': '), ensure_ascii=False)
        f.write(_str)

