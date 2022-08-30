package main

import (
	"fmt"
)

func main() {
	var fname, name string
	fmt.Println("あなたのお名前は(性 名)?")
	fmt.Scanln(&fname, &name)

	var age int
	fmt.Println("あなたの年齢は?")
	fmt.Scanf("%d", &age)

	fmt.Printf("名前:%s %s 年齢:%d\n", fname, name, age)
}
