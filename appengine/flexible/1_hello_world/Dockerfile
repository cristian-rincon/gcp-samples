FROM python:3.8-alpine
WORKDIR /app
ENV FLASK_APP=$WORKDIR/main.py
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY main.py main.py
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8080"]
