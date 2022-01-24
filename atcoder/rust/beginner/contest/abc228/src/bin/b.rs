fn main() {
    proconio::input! {
        n: usize,
    mut x: usize,
       an: [usize; n],
    }

    // println!("{}", x);
    // println!("{:?}", an);

    let mut secrets = vec![0; n];

    loop {
        // 秘密を話す相手
        let a = an[x-1];
        // 秘密を知っているかどうか
        let is_secrets = secrets[x-1];
        // 知っていれば終了
        if is_secrets == 1 {
            break;
        }
        secrets[x-1] = 1;
        x = a;
    }
    println!("{}", secrets.iter().sum::<i32>());
}
