FROM python:3.7-stretch

RUN apt-get update && apt-get install -y postgresql

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . ./

ENV FLASK_APP=nemo

EXPOSE 5000

CMD /usr/src/app/bin/entrypoint.sh
