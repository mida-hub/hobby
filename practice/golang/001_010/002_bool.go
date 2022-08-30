package main

import "fmt"

func main() {
	// bool型の変数を宣言
	var b bool
	b = true
	fmt.Println(b)
	b = false
	fmt.Println(b)
	b = true || false
	fmt.Println(b)
	b = true && false
	fmt.Println(b)
}
