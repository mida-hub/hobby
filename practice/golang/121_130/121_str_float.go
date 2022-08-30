package main

import (
	"fmt"
	"strconv"
)

func main() {
	s := "123.456789"
	f64, err := strconv.ParseFloat(s, 32)

	fmt.Println(float32(f64), err)
}
