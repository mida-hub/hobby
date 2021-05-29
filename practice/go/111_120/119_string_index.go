package main

import (
	"fmt"
	"strings"
)

func main() {
	s := "The Go Programming Language"

	fmt.Println(strings.Index(s, "Go"))
	fmt.Println(strings.Index(s, "xxx"))
}
