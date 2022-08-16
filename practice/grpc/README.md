# tutorial
https://grpc.io/docs/languages/go/quickstart/
go install google.golang.org/protobuf/cmd/protoc-gen-go@v1.28
go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@v1.2

export PATH="$PATH:$(go env GOPATH)/bin"
cd grpc-go/examples/helloworld

# setup
## protobuf
brew install protobuf

## grpc-cli
brew tap grpc/grpc
brew install grpc

## go
mkdir api
cd api
go mod init pancake.maker

go get -u github.com/golang/protobuf/protoc-gen-go
go get google.golang.org/grpc
go get google.golang.org/grpc/reflection

go get -u go.uber.org/zap
go get -u github.com/grpc-ecosystem/go-grpc-middleware

## path
tree . -L 1

grpc
├── README.md
├── api
├── client
└── proto

protoc \
    -Iproto \
    --go_out=plugins=grpc:api \
    proto/*.proto
