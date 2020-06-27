FROM ubuntu:latest
RUN apt-get update && apt-get install -y \
	sudo \
	wget \
	vim
# root権限意外でも扱えるようにする 共有サーバとか
WORKDIR /opt

# 任意のversionをinstall
# -b -p インタラクティブ操作を回避
# /opt/anaconda3　インストール先
RUN wget https://repo.continuum.io/archive/Anaconda3-2020.02-Linux-x86_64.sh && \
	sh Anaconda3-2020.02-Linux-x86_64.sh -b -p /opt/anaconda3 && \
	# インストール後必要ないから削除
	rm -f Anaconda3-2020.02-Linux-x86_64.sh

# pythonを扱えるようにpathを通す
# /opt/anaconda3/bin 配下に $PATHを通す　
# $PATH 既存のPATHに追加している
ENV PATH /opt/anaconda3/bin:$PATH

# 今後 pip installで追加したいpackageがある時のため
RUN pip install --upgrade pip
# jupyterを実行する rootに移動後自分だけやから
WORKDIR /
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--LabApp.token=''"]