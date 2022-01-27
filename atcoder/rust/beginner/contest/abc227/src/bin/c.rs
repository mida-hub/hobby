fn main() {
    proconio::input! {
        n: usize,
    }

    // println!("{}", n);

    let mut ans = 0;
    for a in 1..=n {
        if a * a * a > n { break; }
        for b in a..=n {
            if a * b * b > n { break; }
            let c = n / (a * b);
            if b <= c {
                ans += c - b + 1;
            }
        }
    }
    println!("{}", ans);
}
