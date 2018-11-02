FROM ubuntu:bionic

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y python3 python3-pip postgresql libpq-dev nodejs npm

RUN mkdir -p /var/nemo
WORKDIR /var/nemo

COPY requirements.txt ./
COPY package.json ./

RUN pip3 install -r requirements.txt
RUN npm install

# add app
COPY bin ./bin
COPY nemo ./nemo
COPY .babelrc ./
COPY setup.py ./
COPY webpack.config.js ./

EXPOSE 5000
EXPOSE 5001

CMD /var/nemo/bin/entrypoint.sh
