package main

import (
	"fmt"
	"time"
)

func main() {
	fmt.Println(time.Now())
	time.Sleep(time.Second * 10)
	fmt.Println(time.Now())
}
