FROM python:3.10

EXPOSE 5004

RUN mkdir -p /opt/services/bots/s-bot
WORKDIR /opt/services/bots/s-bot


COPY . /opt/services/bots/s-bot/

RUN pip install -r requirements.txt

CMD ["python", "/opt/services/bots/s-bot/main.py"]
