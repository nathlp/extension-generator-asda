FROM python:3.8-slim-buster

WORKDIR /gerador

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY tela.py tela.py
COPY geradorR.py geradorR.py
COPY geradorPython.py geradorPython.py
COPY geradorJava.py geradorJava.py
COPY /modelos modelos
COPY /images images
COPY /gabaritos gabaritos
COPY /codigo codigo
COPY /classes classes


CMD [ "python3", "tela.py" ]