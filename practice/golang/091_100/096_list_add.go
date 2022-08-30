package main

import (
	"container/list"
	"fmt"
)

func main() {
	l1 := list.New()
	l2 := list.New()

	for i := 0; i < 5; i++ {
		l1.PushBack(i)
		l2.PushBack(i)
	}

	l1.PushBackList(l2)

	for e := l1.Front(); e != nil; e = e.Next() {
		fmt.Println(e.Value)
	}
}

func getElement(l *list.List, index int) *list.Element {
	for e, i := l.Front(), 0; e != nil; e = e.Next() {
		if i == index {
			return e
		}
		i++
	}
	panic("インデックス不正")
}
