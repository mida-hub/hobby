fn to_int(s: String) -> i64 {
    s.parse::<i64>().unwrap()
}

fn get_nth_char_from_string(s: &String, index: usize) -> char {
    s.chars().nth(index).unwrap()
}

fn main() {
    proconio::input! {
        s: String,
    }
    let a = to_int(get_nth_char_from_string(&s, 0).to_string());
    let c = to_int(get_nth_char_from_string(&s, 2).to_string());
    println!{"{}", a * c};
}
