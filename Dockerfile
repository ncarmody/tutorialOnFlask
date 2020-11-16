FROM python:3.7.9

WORKDIR /user/src/app

RUN python -m pip install --upgrade pip

COPY './requirements.txt' .

RUN pip install -r requirements.txt

EXPOSE 5000

COPY . .

ENTRYPOINT ["python", "app.py"]