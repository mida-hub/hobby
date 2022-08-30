package main

import (
	"fmt"
	"math"
)

func main() {
	var degree float64 = 45
	radian := degree * math.Pi / 180

	fmt.Println(radian)
	fmt.Println(math.Sin(radian))
	fmt.Println(math.Cos(radian))
	fmt.Println(math.Tan(radian))
}
