package main

// 構造体と関数を紐付ける

import "fmt"

type Account struct {
	ID       int
	Name     string
	Password string
}

// アカウント登録
func (account Account) Create() Account {
	// db.Insert(account)
	fmt.Println("create")
	// insert 後に付与された ID をセットするなどが必要
	account.ID = 1
	return account
}

// アカウント情報更新
func (account Account) Update() Account {
	// db.Update(account.ID, account)
	fmt.Println("update")
	return account
}

// アカウント情報取得
// 本当は引数に ID が必要
func (account Account) Read() Account {
	// db.Get(account.ID)
	fmt.Println("read")
	return account
}

// アカウント削除
func (account Account) Delete() {
	// db.Delete(account.ID)
	fmt.Println("delete")
}

func main() {
	account := Account{
		Name:     "gotaro",
		Password: "5go5go5go5go",
	}

	account = account.Create()
	fmt.Println(account)
	account = account.Update()
	account = account.Read()
	account.Delete()
}
