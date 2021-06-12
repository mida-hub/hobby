fn main() {
    for count in 0..10{
        println!("count: {}", count);
    };

    let array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
    for element in &array{
        println!("element: {}", element);
    };

}
