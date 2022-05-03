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
    println!("{:?}", make_divisors(&(10 as usize)));
    println!("{:?}", make_divisors(&(25 as usize)));
    println!("{:?}", make_divisors(&(31 as usize)));
    println!("{:?}", make_divisors(&(655 as usize)));
}
