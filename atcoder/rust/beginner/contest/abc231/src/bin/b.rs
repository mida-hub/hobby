use std::collections::HashMap;

fn main() {
    proconio::input! {
        n: usize,
        sn: [String; n],
    }

    // println!("{}", n);
    // println!("{:?}", sn);

    let mut votes: HashMap<&str, i32> = HashMap::new();
    for s in &sn {
        // key, value の組み合わせでカウントする
        *votes.entry(s).or_insert(0) += 1;
    }
    // println!("{:?}", votes);
    let mut votes_vec: Vec<(&&str, &i32)> = votes.iter().collect();
    // value の降順にする
    votes_vec.sort_by(|a, b| (-a.1).cmp(&(-b.1)));
    // println!("{:?}", votes_vec);
    println!("{}", votes_vec[0].0);
}
