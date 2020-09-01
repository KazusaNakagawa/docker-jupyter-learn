# docker learn
## sample Dockerfle jupyter lab
- Dokcerfile作成メモ 

## create build image
```
$ docker build -t jupyter_lab:latest .
```

## コンテナ作成 with マウント
```
$ docker run -p 8888:8888 -v <host path>:<local path> --name my-lab jupyter_lab /bin/bash
```

## 再度コンテナ起動
```
$ docker start <container name>
```
