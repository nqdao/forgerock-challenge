FROM python

WORKDIR /app

COPY requirements.txt /app/

RUN python -m pip install --upgrade pip \
    && python3 -m pip install -r requirements.txt

COPY . /app/

EXPOSE 5000

CMD ["python", "server.py"]
