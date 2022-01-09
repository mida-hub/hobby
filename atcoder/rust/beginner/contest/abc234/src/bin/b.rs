fn main() {
    proconio::input! {
        n: u128,
        xy: [[i32; 2]; n],
    };
    println!("{}", n);
    println!("{:#?}", xy);
}
