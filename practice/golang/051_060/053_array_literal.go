package main

import "fmt"

func main() {
	array1 := [5]float32{}
	array2 := [6]int{1, 2, 3, 4}
	// ...と記述すると要素数が長さとして使用される
	array3 := [...]string{"One", "Two", "Three"}

	fmt.Println(array1)
	fmt.Println(array2)
	fmt.Println(array3)
}
