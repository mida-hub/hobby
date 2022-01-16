fn to_bin(v: i64) -> String {
    format!("{:b}", v).to_string()
}

fn to_int(s: String) -> i64 {
    s.parse::<i64>().unwrap()
}

// 二重配列 abc233 c
let mut ans = Vec::new();
let v = Vec::new();
ans.push(v);
ans[0].push(1);

// hashmap
// https://yiskw713.hatenablog.com/entry/rust-hashmap-sort
