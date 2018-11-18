FROM python:3.6.7

# add requirements.txt to the image
#ADD requirements.txt /reqs/requirements.txt

RUN mkdir /app
# set working directory to /app/
WORKDIR /app
COPY requirements.txt /app/requirements.txt

# install python dependencies
RUN pip install -r requirements.txt


