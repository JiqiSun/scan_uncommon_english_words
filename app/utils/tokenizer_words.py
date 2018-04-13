from nltk.tokenize import RegexpTokenizer


def get_tokenized_words(contents):
    tokenizer = RegexpTokenizer(r'[a-zA-Z]+')
    words = tokenizer.tokenize(contents)
    return words
