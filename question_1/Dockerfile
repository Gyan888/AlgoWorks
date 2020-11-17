FROM python:3.6.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirement.txt /code/
ADD start.sh /code/
ADD tasks.py /code/
RUN pip install -r requirement.txt


