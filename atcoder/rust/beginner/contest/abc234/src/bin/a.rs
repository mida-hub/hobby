fn fx(x: i32) -> i32 {
    x * x + 2 * x + 3
}

fn main() {
    proconio::input! {
        t: i32,
    }
    let ans = fx(fx(fx(t) + t) + fx(fx(t)));
    println!("{}", ans);
}
