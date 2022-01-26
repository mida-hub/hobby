use std::collections::HashMap;

fn main() {
    proconio::input! {
            n: usize,
            a4n: [usize; 4*n-1],
        }

    let mut check: HashMap<&usize, usize> = HashMap::new();

    for a in &a4n {
        *check.entry(a).or_insert(0) += 1;
    }
    // println!("{:?}", check);
    let mut check_vec: Vec<(&&usize, &usize)> = check.iter().collect();
    check_vec.sort_by(|a, b| a.1.cmp(&b.1));
    println!("{}", check_vec[0].0);
}
