# docker learn
## sample Dockerfle jupyter lab
- Dokcerfile作成メモ 

## index
- [1.create build image](#1.create build image)
- [2.when docker-compose](#2.when docker-compose)

## 1.create build image
```
$ docker build -t jupyter_lab:latest .
```

## コンテナ作成 with マウント
```
$ docker run -p 8888:8888 -v <host path>:<local path> --name my-lab jupyter_lab
```

## 操作コマンドメモ
- コンテナ停止
```
$ docker stop my-lab
```
- 再度コンテナ起動

```
$ docker start <container name>
```
- コンテナ内に入る(起動時, bash付与)

```
$ docker exec -it my-lab bash
```

- ※コンテナ消滅

```
$ docker down <container name>
```

## 2.when docker-compose

- In the working directory `Dockerfile`, `docker-compose.yml`
```
$ docker-compose build
```

- create container
```
$ docker-compose up -d
```

- check State: Up
```
$ docker-compose ps
$ docker-compose ps -a
```
>if State: Exit 0
```
$ dokcer-compose start
```

- コンテナ内に入るなら

```
$ docker-compose exec web bash
```

## browser accsess
http://localhost:8888/

