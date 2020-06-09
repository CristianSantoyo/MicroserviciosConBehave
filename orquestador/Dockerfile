FROM python:3.6

EXPOSE 2020

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY orquestador.py /app
CMD python orquestador.py