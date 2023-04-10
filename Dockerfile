FROM python:3.10.2

WORKDIR /app

# RUN python -m pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


COPY wsgi.py wsgi.py
COPY blog ./blog

RUN flask db init
RUN flask db upgrade
RUN flask create-admin
RUN flask create-tags

EXPOSE 5000

CMD ["python", "wsgi.py"]
