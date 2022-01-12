fn to_bin(v: i64) -> String {
    format!("{:b}", v).to_string()
}

fn to_int(s: String) -> i64 {
    s.parse::<i64>().unwrap()
}
