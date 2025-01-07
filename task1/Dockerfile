# Forward 5252 to 5252
FROM ubuntu

WORKDIR /app

RUN apt-get update && \
    apt-get upgrade -y

RUN apt-get install -y python3 

RUN rm /usr/lib/python*/EXTERNALLY-MANAGED

RUN apt-get install -y pip && \
    pip3 install flask

COPY ./api.py .

EXPOSE 5252

ENTRYPOINT [ "python3", "api.py" ]