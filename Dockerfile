FROM python:3

ENV PYTHONUNBUFFERED 1
ENV SUBURL default

RUN mkdir /code
COPY ./cua/requirements.txt /code
RUN pip install -r /code/requirements.txt
COPY ./cua /code
WORKDIR /code

EXPOSE 80
EXPOSE 443
ENTRYPOINT /usr/bin/python
CMD ["./manage.py", "runserver", "0.0.0.0:80"]

