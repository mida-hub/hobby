fn main() {
    proconio::input! {
        n: u128,
        xy: [[i32; 2]; n],
    };

    let mut ans = 0 as f64;
    for i in 0..n {
        for j in (i+1)..n {
            // if i == j {continue;}
            let x1 = xy[i as usize ][0];
            let y1 = xy[i as usize ][1];
            let x2 = xy[j as usize ][0];
            let y2 = xy[j as usize ][1];
            let line = (((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) as f64).sqrt();

            if line > ans {
                ans = line
            }
        }
    }
    println!("{}", ans);
}
