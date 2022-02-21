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
let mut votes_vec: Vec<(&&usize, &usize)> = votes.iter().collect();
// sort asc
votes_vec.sort_by(|a, b| a.1.cmp(&b.1));
// sort desc
votes_vec.sort_by(|a, b| (-a.1).cmp(&(-b.1)));

// 存在する
if votes.get(s) {}
// 存在しない
if votes.get(s) == None {}

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

// 文字列の入れ替え
use proconio::marker::{Chars, Usize1};

fn main () {
    proconio::input! {
    mut s: Chars,
        a: Usize1,
        b: Usize1,
    }
    s.swap(a, b);
    println!("{}", s.iter().collect::<String>());
}
