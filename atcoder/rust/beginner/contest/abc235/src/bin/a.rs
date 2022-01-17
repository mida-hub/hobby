fn to_int(s: String) -> i64 {
    s.parse::<i64>().unwrap()
}

fn main() {
    proconio::input! {
        abc: String,
    }

    let a = to_int(abc.chars().nth(0).unwrap().to_string());
    let b = to_int(abc.chars().nth(1).unwrap().to_string());
    let c = to_int(abc.chars().nth(2).unwrap().to_string());
    let ans = a * 100 + b * 10 + c + b * 100 + c * 10 + a + c * 100 + a * 10 + b;
    println!("{}", ans);
}
