fn to_bin(v: i64) -> String {
    format!("{:b}", v).to_string()
}

fn to_int(s: String) -> i64 {
    s.parse::<i64>().unwrap()
}

fn main() {
    proconio::input! {
        k: i64,
    };

    let str_bin_k = to_bin(k);
    let mut ans = "".to_string();
    for s in str_bin_k.chars() {
        // println!("{}", s);
        // 文字列から整数変換->2倍する->文字列に直す
        ans.push_str(&(2 * to_int(s.to_string())).to_string());
    }
    println!("{}", ans);
}
