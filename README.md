# docker learn
## sample Dockerfle jupyter lab
- Dokcerfile作成メモ 

## create build image
```
$ docker build -t jupyter_lab:latest .
```

## コンテナ作成 with マウント
```
$ docker run -p 8888:8888 -v <host path>:<local path> --name my-lab jupyter_lab
```

## コンテナ停止
```
$ docker stop my-lab
```

## 再度コンテナ起動
```
$ docker start <container name>
```

## コンテナ内に入る(起動時, bash付与)
```
$ docker exec -it my-lab bash
```

## ※コンテナ消滅
```
$ docker down <container name>
```