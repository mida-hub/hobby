package main

import "fmt"

func main() {
	for i := 0; i < 5; i++ {
		if i%2 != 0 {
			fmt.Println(i, "奇数")
		} else {
			fmt.Println(i, "偶数")
		}

	}
}
