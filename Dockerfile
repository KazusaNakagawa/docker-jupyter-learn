FROM ubuntu:latest
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libavcodec-extra \
    mysql-client \
    sudo \
    vim \
    wget
	
# root権限意外でも扱えるようにする 共有サーバとか
WORKDIR /opt

# 任意のversionを変数に格納
ENV ANACOND_ARCHIVE=Anaconda3-2022.05-Linux-x86_64.sh

RUN wget https://repo.continuum.io/archive/$ANACOND_ARCHIVE && \
    sh $ANACOND_ARCHIVE -b -p /opt/anaconda3 && \
    rm -f $ANACOND_ARCHIVE

ENV PATH /opt/anaconda3/bin:$PATH

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

WORKDIR /
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--LabApp.token=''"]
