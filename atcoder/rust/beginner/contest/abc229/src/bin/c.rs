fn main() {
    proconio::input! {
        n: usize,
        mut w: usize,
        mut abn: [[usize; 2]; n]
    }

    // println!("{},{}", n, w);
    // println!("{:?}", abn);

    abn.sort_by(|a, b| b.cmp(&a));
    // println!("{:?}", abn);

    let mut ans = 0;
    for abi in &abn {
        let a = abi[0];
        let b = abi[1];

        if w >= b {
            w -= b;
            ans += a * b;
        } else {
            ans += a * w;
            w = 0;
        }
        // println!("a:{}, b:{}", a, b);
        // println!("w:{}", w);
        // println!("ans:{}", ans);
    }

    println!("{}", ans);
}
