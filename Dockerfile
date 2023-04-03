FROM python:3.11.2
WORKDIR /alice
COPY . /Alice
RUN pip install -r requirements.txt
CMD ["python", "bot.py"]