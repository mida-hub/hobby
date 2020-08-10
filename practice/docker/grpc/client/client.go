package main

import (
	"context"
	"fmt"
	"log"

	cat "../pb"

	"google.golang.org/grpc"
)

func main() {
	conn, err := grpc.Dial("localhost:1234", grpc.WithInsecure())
	if err != nil {
		log.Fatal("connection error:", err)
	}
	defer conn.Close()

	client := cat.NewCatClient(conn)
	// message := &cat.GetMyCatMessage{TargetCat: "mike"}
	message := &cat.GetMyCatMessage{TargetCat: "tama"}
	res, err := client.GetMyCat(context.Background(), message)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("result:%s\n", res)
}
