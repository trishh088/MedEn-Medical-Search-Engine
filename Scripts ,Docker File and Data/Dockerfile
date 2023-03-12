FROM python:3.9
EXPOSE 8504
WORKDIR /meden
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -y
RUN apt install libgl1-mesa-glx -y
RUN apt-get install 'ffmpeg'\
    'libsm6'\
    'libxext6'  -y

COPY requirements.txt ./requirements.txt
RUN pip3 install matplotlib==3.4.3
RUN pip3 install protobuf==3.19.0
RUN pip3 install -r requirements.txt
COPY . .
CMD streamlit run app.py    
