package main

import (
    "fmt"
    "log"
    "net"
    "os"
    "os/signal"

    "google.golang.org/grpc"
    "google.golang.org/grpc/reflection"

    "grpc/api/handler"
    "grpc/api/gen/api"

    "go.uber.org/zap"
    "github.com/grpc-ecosystem/go-grpc-middleware"
    "github.com/grpc-ecosystem/go-grpc-middleware/logging/zap"
)

func main() {
    port := 50051
    lis, err := net.Listen("tcp", fmt.Sprintf(":%d", port))
    if err != nil {
        log.Fatalf("failed to listen: %v", err)
    }

    zapLogger, err := zap.NewProduction()
    if err != nil {
        panic(err)
    }
    grpc_zap.ReplaceGrpcLogger(zapLogger)

    server := grpc.NewServer(
        grpc.UnaryInterceptor(
            grpc_middleware.ChainUnaryServer(
                grpc_zap.UnaryServerInterceptor(zapLogger),
            ),
        ),
    )
    
    api.RegisterPancakeBakerServiceServer(
        server,
        handler.NewBakerHandler(),
    )
    reflection.Register(server)

    go func() {
        log.Printf("start gRPC server port: %v", port)
        server.Serve(lis)
    }()

    quit := make(chan os.Signal)
    signal.Notify(quit, os.Interrupt)
    <-quit
    log.Println("stopping gRPC server...")
    server.GracefulStop()
}
