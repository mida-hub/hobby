fn main() {
    let mut count = 0;
    let result = loop {
        println!("count: {}", count);
        count += 1;
        if count == 10 {
            break count;
        }
    };
    println!("result: {}", result);
}
