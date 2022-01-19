// 数値型に変換する
fn to_int(s: String) -> i64 {
    s.parse::<i64>().unwrap()
}

fn main() {
    proconio::input! {
        a: String,
        b: String,
    }

    let a_rev = a.chars().rev().collect::<String>();
    let b_rev = b.chars().rev().collect::<String>();

    let a_len = a.len();
    let b_len = b.len();

    let min_len = if a_len >= b_len { b_len } else { a_len };
    
    let mut ans = false;
    for i in (0..min_len) {
        let ai  = a_rev.chars().nth(i).unwrap().to_string();
        let bi  = b_rev.chars().nth(i).unwrap().to_string();

        // println!("{},{}", ai, bi);
        if to_int(ai) + to_int(bi) > 9 {
            ans = true;
        }
    }
    if ans {
        println!("Hard");
    } else {
        println!("Easy");
    }
}
