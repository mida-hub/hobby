# 準備
## cf.
https://tech.libinc.co.jp/entry/2019/11/07/111548

## gRPC
```
go get -u google.golang.org/grpc
```

## protoc
```
brew install protobuf
```

## protoc-gen-go
```
go get -u github.com/golang/protobuf/protoc-gen-go
```

# Docoker
## docker-compose
```
docker-compose up -d
docker exec -it study-grpc bash
protoc --go_out=plugins=grpc:. ./pb/cat.proto

go build server.go
./server

go build client.go
./client
```


