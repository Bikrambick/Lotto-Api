FROM python:3.6
MAINTAINER Adolfo Lopez (adolfolopez88@gmail.com) 

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y 

WORKDIR /app
COPY . ./

RUN pip3 install -r requirements.txt


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000
