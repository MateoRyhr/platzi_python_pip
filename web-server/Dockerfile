FROM python:3.12.6

WORKDIR /csv

COPY requeriments.txt /csv/requeriments.txt

RUN pip install --no-cache-dir --upgrade -r /csv/requeriments.txt

COPY . /csv

CMD bash -c "while true; do sleep 1; done"