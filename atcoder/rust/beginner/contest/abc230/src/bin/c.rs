use std::collections::HashMap;

fn main() {
    proconio::input! {
        n: isize,
        a: isize,
        b: isize,
        p: isize,
        q: isize,
        r: isize,
        s: isize,
    }
    // println!("{},{},{}", n, a, b);
    // println!("{},{},{},{}", p, q, r, s);

    let mut matrix: HashMap<String, bool> = HashMap::new();

    let i_from = std::cmp::max(p - a, r - b);
    let i_to   = std::cmp::min(q - a, s - b);

    for i in i_from..=i_to {
        let ak = a + i;
        let bk = b + i;
        let key = (ak).to_string() + "-" + &(bk).to_string();
        *matrix.entry(key).or_insert(true) = true;
    }

    let i_from = std::cmp::max(p - a, b - s);
    let i_to   = std::cmp::min(q - a, b - r);

    for i in i_from..=i_to {
        let ak = a + i;
        let bk = b - i;
        let key = (ak).to_string() + "-" + &(bk).to_string();
        *matrix.entry(key).or_insert(true) = true;
    }

    // println!("{:?}", matrix);

    for i in p..=q {
        for j in r..=s {
            // println!("{},{}", i,j);
            let key = (i).to_string() + "-" + &(j).to_string();
            if matrix.get(&key) != None {
                print!("#");
            } else {
                print!(".");
            }
        }
        println!("");
    }
}
