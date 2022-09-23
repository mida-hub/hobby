package main

import "fmt"

const (
	AAA int = iota
	BBB
	CCC
)

func main() {
	fmt.Println("iota test")
	fmt.Printf("AAA=%d\n", AAA)
	fmt.Printf("BBB=%d\n", BBB)
	fmt.Printf("CCC=%d\n", CCC)
}
