# pandas memo
## directory structure
-  ds_python/ : doc file

## sample Dockerfle (jupyter lab)

### index
- [1.Dockerfile](#1dockerfile)
- [2.docker-compose](#2docker-compose)
- [3.M1 Mac](#3m1-mac)

### 1.Dockerfile
```
$ docker build -t jupyter_lab:latest .
```

### コンテナ作成 with マウント
```
$ docker run -p 8888:8888 -v <host path>:<container path> --name my-lab jupyter_lab
```

### 操作コマンドメモ
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

### 2.docker-compose

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

### 3.M1 Mac

#### option (--platform linux/amd64) つけて実行

```bash
$ docker build --platform linux/amd64 -t jupyter_lab:latest .
```

#### mount
```bash
$ docker run -p 8888:8888 -v <host path>:<container path> --name my-lab jupyter_lab
```

#### 再度入る
```
$ docker start <container name>
```

## browser accsess
http://localhost:8888/

