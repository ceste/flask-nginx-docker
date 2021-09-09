FROM tiangolo/uwsgi-nginx-flask:python3.8

ENV UWSGI_INI /app/uwsgi.ini

# copy over our requirements.txt file
COPY requirements.txt /tmp/

# upgrade pip and install required python packages
RUN pip install -U pip
RUN pip install -r /tmp/requirements.txt

# copy over our app code
COPY . /app

ENV LISTEN_PORT 5001

EXPOSE 5001
