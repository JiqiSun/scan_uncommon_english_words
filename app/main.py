from flask import Flask, render_template, request, redirect, url_for
from models import *
from utils.table_generator import table_generator

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def show():
    new_words = get_new_words() or []
    article = get_article() or ''
    if request.method == 'POST':
        if request.form['article']:
            contents = request.form['article']
            new_words = filter_words(contents)
            data = {'article': [{'contents': contents}, {'newWords': new_words}]}
            write_db(data)
            article = contents
    words_table = table_generator(new_words, 5)
    return render_template('index.html', words=new_words, article=article, table=words_table)


@app.route("/add", methods=['POST'])
def add_known_words():
    new_words = get_new_words()
    article = get_article()
    known_words = []
    if request.method == 'POST':
        if request.form['words']:
            known_words = request.form.getlist('words')
            add_words(known_words)
    new_words = [word for word in new_words if word not in known_words]
    data = {'article': [{'contents': article}, {'newWords': new_words}]}
    write_db(data)
    return redirect(url_for('show'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)

