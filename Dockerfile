FROM python

WORKDIR /

COPY . /app

RUN pip install -r requirements.txt