fn main() {
    proconio::input! {
        n: u128,
        x: u128,
        a: [[u128]; n]
    };

    let mut ans = Vec::new();
    let v = Vec::new();
    ans.push(v);
    ans[0].push(1);
    
    let mut row = 1;
    for i in 0..n {
        let v = Vec::new();
        ans.push(v);
        for ai in &a[i as usize] {
            let len_ans = ans[row-1].len();
            for j in 0..len_ans {
                let mul = ans[(row-1) as usize][j as usize] * ai;
                ans[row].push(mul);
            }
        }
        row += 1;
    }
    let last_ans = ans[n as usize].iter().filter(|&&ai| ai == x).count();
    println!("{:?}", last_ans);
}
