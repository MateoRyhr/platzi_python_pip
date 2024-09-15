FROM python:3.12.6

WORKDIR /csv

COPY requirements.txt /csv/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /csv/requirements.txt

COPY . /csv

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
# CMD bash -c "uvicorn; main:app; --host; 0.0.0.0; --port; 80;"