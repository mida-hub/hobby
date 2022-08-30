package main

import "fmt"

func main() {
	a, b := 1, 1
	double(a, &b)

	// aは値渡しなので変わらない, bは参照渡しなので値が変わる
	fmt.Println(a)
	fmt.Println(b)
}

func double(x int, y *int) {
	x *= 2
	*y *= 2
}
