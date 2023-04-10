FROM python:3.10.2

WORKDIR /app

# RUN python -m pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


COPY wsgi.py wsgi.py
COPY blog ./blog

RUN flask init-db
RUN flask create-admin

EXPOSE 5000

CMD ["python", "wsgi.py"]
