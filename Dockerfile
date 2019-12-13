FROM python:2.7
LABEL maintaner="Liyuzhi"
COPY . /app/
WORKDIR /app
RUN pip install flask redis
EXPOSE 5000
CMD ["python","app.py"]

