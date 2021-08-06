FROM python:3.9

LABEL maintainer="Rohit Warke <rohitswarke@gmail.com>"

RUN mkdir app
 
COPY . app/

WORKDIR app

RUN pip install -r requirements.txt

EXPOSE 8086

#ENV PYTHONPATH=/

CMD ["python","-m", "city_details"]

