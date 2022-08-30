package main

import "fmt"

type myType int

func (value myType) setByValue(newValue myType) {
	// 無意味
	value = newValue
}

func (value *myType) setByPointer(newValue myType) {
	// 値は反映される
	*value = newValue
}

func main() {
	var x myType = 0

	x.setByValue(1)
	fmt.Println(x)

	x.setByPointer(2)
	fmt.Println(x)
}