package main

import (
	"encoding/json"
	"log"
	"net/http"
)

type Ping struct {
	Status int    `json:"status"`
	Result string `json:"result"`
}

func rootHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")

	// get できるように変更する
	// w.Header().Set("Access-Control-Allow-Origin", "*")
	// Cookie 取得を有効にするための設定
	w.Header().Set("Access-Control-Allow-Origin", "http://localhost:9999")

	// Cookie 取得を有効にするための設定
	w.Header().Set("Access-Control-Allow-Credentials", "true")

	// プリフライトエラーを解消する
	w.Header().Set("Access-Control-Allow-Headers", "Content-Type")

	// Cookie 取得
	cookie, _ := r.Cookie("hoge")
	var result string
	if cookie != nil {
		result = cookie.Value
	} else {
		result = "Cookie 取得できませんでした"
	}

	ping := Ping{http.StatusOK, result}
	res, _ := json.Marshal(ping)

	w.Write(res)
}

func main() {
	var httpServer http.Server
	http.HandleFunc("/", rootHandler)
	httpServer.Addr = ":8888"
	log.Println(httpServer.ListenAndServe())
}

// curl http://localhost:8888
// -> {"status":200,"result":"ok"}
