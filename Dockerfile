FROM python:3
WORKDIR /Alice
COPY . .
RUN python3 -m pip install -U bot.py python-dotenv
CMD python -u ./bot.py
