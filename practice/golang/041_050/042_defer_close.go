package main

import (
	"os"
)

// ファイルが存在しない場合はあいうえおで作成
// ファイルが存在する場合はあいうえおで上書き
// ただし15byte分を強制的に書き換えるので破損する可能性がある
func main() {
	// ファイルオープン
	file, err := os.OpenFile("test.txt", os.O_WRONLY|os.O_CREATE, 0666)

	// オープンに失敗したときは終了
	if err != nil {
		os.Exit(1)
	}

	defer file.Close()

	file.WriteString("あいうえお")
}
