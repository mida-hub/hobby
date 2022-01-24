use std::collections::HashMap;

fn main() {
    proconio::input! {
        n: usize,
        sn: [i32; n],
    }

    let mut sn_list: HashMap<i32, i32> = HashMap::new();

    for a in 1..142 {
        for b in 1..142 {
            let si = 4 * a * b + 3 * a + 3 * b;
            if si > 1000 {
                break;
            }
            // println!("{}", ab);
            *sn_list.entry(si).or_insert(0) += 1;
        }
    }
    
    let mut ans = 0;
    for s in &sn {
        *sn_list.entry(*s).or_insert(0) += 1;
        
        if sn_list[s] == 1 {
            ans += 1;
            *sn_list.entry(*s).or_insert(0) -= 1;
        }
        // println!("{}", s);
        // println!("{}", sn_list[s]);
    }

    println!("{}", ans);
}
