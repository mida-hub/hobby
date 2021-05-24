package main

import "fmt"

// chan チャネル
// chan <- 送信専用
// <- chan 受信専用

func main() {
	c := make(chan int)

	// 送信
	go func(s chan<- int) {
		for i := 0; i < 5; i++ {
			s <- i
		}
		close(s)
	}(c)

	// 受信
	for {
		value, ok := <-c

		if !ok {
			break
		}

		fmt.Println(value)
	}
}
