package main

import (
	"fmt"
	"time"
)

func main() {
	for day := time.Sunday; day <= time.Saturday; day++ {
		switch day {
		case time.Sunday:
			fallthrough // 続けて直下のcase文が実行される
		case time.Saturday:
			fmt.Println(day, "休日")
		default:
			fmt.Println(day, "たぶん平日")
		}
	}
}
