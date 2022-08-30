package main

import (
	"fmt"
	"time"
)

func main() {
	start := time.Now()
	fmt.Println(start)
	time.Sleep(time.Second * 5)
	end := time.Now()
	fmt.Println(end)

	sub := end.Sub(start)
	fmt.Println(sub)
	fmt.Println(int(sub/time.Second), "秒")
}
