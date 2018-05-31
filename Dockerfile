FROM python:3.5

ENV PORT=3000

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 3000

ENTRYPOINT ["python3"]

RUN python3 setup.py install

CMD ["-m", "swagger_server"]