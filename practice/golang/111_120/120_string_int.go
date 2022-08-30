package main

import (
	"fmt"
	"strconv"
)

func main() {
	s := "1234567890"

	i64, err := strconv.ParseInt(s, 10, 0)
	fmt.Println(int(i64), err)

	i32, err := strconv.ParseInt(s, 10, 32)
	fmt.Println(int(i32), err)
}
