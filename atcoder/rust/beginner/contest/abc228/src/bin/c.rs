use std::collections::HashMap;
use proconio::marker::{Usize1};

fn main() {
    proconio::input! {
        n: i32,
        k: Usize1,
        pn3: [[i32; 3]; n],
    }

    let mut answers: HashMap<i32, i32> = HashMap::new();
    
    // println!("{},{}", n, k);
    // println!("{:?}", pn3);

    for i in 0..pn3.len() {
        *answers.entry(i as i32).or_insert(0) += pn3[i].iter().sum::<i32>();
    }
    // println!("{:?}", answers);

    let mut answers_vec: Vec<(&i32, &i32)> = answers.iter().collect();
    answers_vec.sort_by(|a, b| (-a.1).cmp(&(-b.1)));
    // println!("{:?}", answers_vec);

    for i in 0..pn3.len() {
        let pi = answers.get(&(i as i32)).unwrap();
        // println!("{}", answers_vec.len());
        let pk = answers_vec[k].1;

        // println!("{:?}", pi);
        // println!("{:?}", pk);
        if pi + 300 >= *pk {
            println!("Yes");
        } else {
            println!("No");
        }
    }
}
