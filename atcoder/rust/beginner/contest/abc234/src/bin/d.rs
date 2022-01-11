fn main() {
    proconio::input! {
        n: usize,
        k: usize,
        mut pn: [i32; n],
    };
    
    let mut is_ans_arr = pn.clone();
    for i in 0..n {
        is_ans_arr[i] = 0;
    }
    for i in 0..k {
        is_ans_arr[(pn[i]-1) as usize] = 1;
    }

    let sorted_pn_i = &mut pn[0..k];
    sorted_pn_i.sort();
    let mut x = sorted_pn_i[0];
    println!("{}", x);

    for i in k..n {
        if pn[i] > x {
            is_ans_arr[(x-1) as usize] = 0;
            is_ans_arr[(pn[i]-1) as usize] = 1;
        }

        while is_ans_arr[(x-1) as usize] == 0 {
            x += 1;
        }
        println!("{}", x);
    }
}
