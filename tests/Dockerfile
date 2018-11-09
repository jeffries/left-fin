# This Dockerfile is built in the top-level context!
FROM nemo_base:latest

WORKDIR /var/nemo

ENV FLASK_ENV=testing

ADD tests/requirements.txt ./requirements.test.txt
RUN pip3 install -r requirements.test.txt

# Copy tests
ADD tests ./tests

# Install application module
RUN python3 setup.py develop

# Copy bootstrap script
WORKDIR /var/nemo
COPY bin/bootstrap.test.sh ./bin/bootstrap.test.sh
COPY bin/bootstrap.util.sh ./bin/bootstrap.util.sh

CMD /var/nemo/bin/bootstrap.test.sh

