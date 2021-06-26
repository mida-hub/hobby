fn main() {
    let s = concat!("A", "b2", 3);
    println!("{}", s);
    let s = format!("{}-{:?}", s, ("D", 5));
    println!("{}", s);
    let s = format!("{}{}", "abc", "def");
    println!("{}", s);
}
