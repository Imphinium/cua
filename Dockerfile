FROM python:3
ENV PYTHONUNBUFFERED 1
ENV SUBURL ''
RUN mkdir /code
COPY ./cua/requirements.txt /code
RUN pip install -r /code/requirements.txt
COPY ./cua /code
WORKDIR /code
EXPOSE 80
EXPOSE 443
SHELL ["/bin/bash", "-c"]
ENTRYPOINT ["python"]
CMD ["./manage.py", "runserver", "0.0.0.0:80"]
