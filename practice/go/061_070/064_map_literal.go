package main

import "fmt"

func main() {
	capitals := map[string]string{
		"日本":   "東京",
		"アメリカ": "ワシントンD.C.",
		"中国":   "北京"}

	fmt.Println(capitals)

	key := "イギリス"
	capital, ok := capitals[key]

	if ok {
		fmt.Println("登録済み", capital)
	} else {
		fmt.Println("未登録", key)
	}
}
