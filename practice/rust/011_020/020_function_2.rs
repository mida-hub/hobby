fn main() {
    let mut x1 = 1;
    println!("x1 = {}", x1);
    x1 = abs(x1);
    println!("abs(x1) = {}", x1);
    let mut x2 = -1;
    println!("x2 = {}", x2);
    x2 = abs(x2);
    println!("abs(x2) = {}", x2);
}

fn abs(number: i32) -> i32 {
    if number < 0 {
        return -number;
    }
    number
}
