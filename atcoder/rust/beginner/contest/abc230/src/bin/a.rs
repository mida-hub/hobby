fn main() {
    proconio::input! {
        n: i64,
    }
    let ans;
    if n >= 42 {
        ans = n + 1;
    } else {
        ans = n;
    }

    println!("{}", format!("AGC{:03}", ans));
}
