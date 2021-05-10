package main

import "fmt"

func main() {
LBL:
	for i := 0; i < 5; i++ {
		fmt.Println(i)

		for j := 0; j < 5; j++ {
			fmt.Println("  ", j)
			if i == j {
				continue LBL
			}
		}
	}
}
