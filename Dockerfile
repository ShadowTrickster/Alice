FROM python:3.11.2
WORKDIR /Alice
COPY . /Alice
RUN pip install -r requirements.txt
CMD ["python", "bot.py"]