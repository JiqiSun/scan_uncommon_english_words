FROM tiangolo/uwsgi-nginx-flask:python3.5

# copy over our requirements.txt file
COPY requirements.txt /tmp/

# upgrade pip and install required python packages
RUN pip install -U pip
RUN pip install -r /tmp/requirements.txt

# install nltk data
RUN  python -m nltk.downloader -d /usr/local/share/nltk_data all

COPY ./app /app
