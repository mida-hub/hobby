fn main() {
    proconio::input! {
        n: usize,
        k: usize,
        a: usize,
    }

    let mut ans = (k + a - 1) % n;
    if ans == 0 {
        ans = n;
    }
    println!("{}", ans);
}
