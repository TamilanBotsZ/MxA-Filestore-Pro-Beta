FROM python:3.8-slim-buster

WORKDIR /MxA-Filestore-Pro-Beta

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "bot.py"]
