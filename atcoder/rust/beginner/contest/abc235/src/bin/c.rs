use std::collections::HashMap;

fn main() {
    proconio::input! {
        n: usize,
        q: usize,
        an: [usize; n],
        xkq: [[usize; 2]; q],
    }

    // println!("{}, {}", n, q);
    // println!("{:?}", an);
    // println!("{:?}", xkq);

    let mut summary_an: HashMap<String, usize> = HashMap::new();
    for i in 0..an.len() {
        // 数字の出現回数を記録する
        let count_key = an[i].to_string();
        *summary_an.entry(count_key).or_insert(0) += 1;

        // HashMapにセットした時点でライフタイムが切れるので再定義
        let count_key = an[i].to_string();
        // 数字の出現回数を取得
        let total_key = summary_an.get(&count_key).unwrap();
        
        // 数字の出現回数ごとに配列の位置をセットする
        let summary_key = count_key + "-" + &total_key.to_string();
        *summary_an.entry(summary_key).or_insert(0) += i+1;
    }
    // println!("{:?}", summary_an);

    for xk in &xkq {
        let serach_key = xk[0].to_string() + "-" + &xk[1].to_string();
        match summary_an.get(&serach_key) {
            Some(result) => println!("{}", result),
            None => println!("-1"),
        }
    }


    // for s in &sn {
    //     // key, value の組み合わせでカウントする
    //     *votes.entry(s).or_insert(0) += 1;
    // }
    // let mut votes_vec: Vec<(&&usize, &usize)> = votes.iter().collect();
    // // sort asc
    // votes_vec.sort_by(|a, b| a.1.cmp(&b.1));
    // // sort desc
    // votes_vec.sort_by(|a, b| (-a.1).cmp(&(-b.1)));
}


// 1 1 2 3 1 2
// 1-1=1
// 1-2=2
// 1-3=5
// 2-1=3
// 2-2=6
// 3-1=4
