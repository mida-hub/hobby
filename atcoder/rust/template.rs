//  binaryに変換する
fn to_bin(v: i64) -> String {
    format!("{:b}", v).to_string()
}

// 数値型に変換する
fn to_int(s: String) -> i64 {
    s.parse::<i64>().unwrap()
}

// 二重配列 abc233 c
let mut ans = Vec::new();
let v = Vec::new();
ans.push(v);
ans[0].push(1);

// hashmap sort
// https://yiskw713.hatenablog.com/entry/rust-hashmap-sort
use std::collections::HashMap;
let mut votes: HashMap<&str, i32> = HashMap::new();
for s in &sn {
    // key, value の組み合わせでカウントする
    *votes.entry(s).or_insert(0) += 1;
}

// 文字列のn番目
abc.chars().nth(0).unwrap()

// 0埋め
println!("{}", format!("AGC{:03}", ans));

// 配列に要素が含まれる
patterns.contains(&s_substr)

// 文字列の反転
let a_rev = a.chars().rev().collect::<String>();

// 配列を作成する
let mut s = vec![0; n];

// 配列の合計
s.iter().sum::<i32>()
