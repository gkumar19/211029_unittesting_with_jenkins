FROM python:3.7
ADD ./ /app

RUN apt-get clean \
    && apt-get -y update
RUN apt-get install -y git

WORKDIR /app

RUN chmod 755 ./entrypoint.sh
CMD [ "./entrypoint.sh" ]