package main

import (
	"fmt"
	"math"
)

func main() {
	val := math.Pi
	fmt.Println(val)
	fmt.Println(math.Ceil(val))
	fmt.Println(math.Floor(val))

	val *= -1
	fmt.Println(val)
	fmt.Println(math.Ceil(val))
	fmt.Println(math.Floor(val))
}
