fn main() {
    proconio::input! {
        n: usize,
        hn: [usize; n],
    }

    let mut ans = 0;
    for hi in &hn {
        if hi > &ans {
            ans = *hi;
        } else {
            break;
        }
    }
    println!("{}", ans);
}
