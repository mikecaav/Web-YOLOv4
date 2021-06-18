FROM pytorch/pytorch:1.4-cuda10.1-cudnn7-runtime
RUN mkdir -p /home/yolov4
COPY . /home/yolov4/
WORKDIR /home/yolov4/ 
RUN apt-get update
RUN apt-get -y install libc-dev
RUN apt-get -y install build-essential
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install -U pip
RUN pip3 install -r requirements.txt

CMD ["python3", "demo.py"]
