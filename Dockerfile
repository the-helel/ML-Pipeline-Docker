FROM centos:latest

RUN yum install python3 -y

RUN pip3 install --upgrade setuptools

RUN pip3 install --upgrade pip

RUN pip3 install Flask

RUN pip3 install pillow

RUN pip3 install numpy

RUN pip3 install keras

RUN pip3 install tensorflow

RUN pip3 install requests

RUN pip3 install Flask[async]

RUN pip3 install opencv-python



WORKDIR /app

COPY . /app

COPY app.py /app


EXPOSE 5000

CMD python3 app.py
