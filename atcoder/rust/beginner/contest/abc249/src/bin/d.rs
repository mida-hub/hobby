fn make_divisors(n: &usize) -> Vec<usize> {
    let mut divisors = Vec::new();
    let mut i = 1 as usize;
    while i * i <= *n {
        if n % i == 0 {
            divisors.push(i);
            if i != (n / i) {
                divisors.push(n / i);
            }
        }
        i += 1;
    }
    return divisors
}

fn main() {
    proconio::input! {
        n: usize,
        an: [usize; n]
        }
    let mut counter_an = vec![0; 200010];
    for ai in &an {
        counter_an[*ai] += 1;
    }
    let mut ans: i64 = 0;
    for ai in &an {
        for aj in make_divisors(ai) {
            ans += counter_an[aj] * counter_an[ai/aj];
        }
    }
    println!("{}", ans);
}
