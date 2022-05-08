fn is_prime(x: usize) -> bool {
    if x < 2 {
        return false
    }
    if x == 2 || x == 3 || x == 5{
        return true // 2,3,5は素数
    }
    if x % 2 == 0 || x % 3 == 0 || x % 5 == 0 {
        return false // 2,3,5の倍数は合成数
    }
    // ためし割り: 疑似素数(2でも3でも5でも割り切れない数字)で次々に割っていく
    let mut prime = 7;
    let mut step = 4;
    while prime * prime <= x {
        if x % prime == 0 {
            return false
        }
        prime += step;
        step = 6 - step;
    }
    return true
}

fn main() {
    proconio::input! {
        n: usize,
    }
    // println!("{}", n);

    let mut primes = Vec::new();
    primes.push(2);
    let mut i = 1;
    while i <= 1000000 {
        if is_prime(i) {
            primes.push(i);
        }
        i += 2;
    }
    // println!("{:?}", primes);

    let mut q = primes.len() - 1;
    let mut ans = 0;
    let mut index = 0;
    for p in &primes {
        while p < &primes[q] && p * primes[q] * primes[q] * primes[q] > n {
            q -= 1;
        }
        if p < &primes[q] {
            index += 1;
            ans += q - index;
        } else {
            break;
        }
    }
    ans += q;

    println!("{}", ans);
}
