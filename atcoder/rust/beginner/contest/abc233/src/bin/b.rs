use proconio::input;

fn main() {
    input! {
        mut l: i32,
        r: i32,
        s: String,
    }
    l -= 1;
    let convert_l = &s[0..l as usize];
    let convert_sub = &s[l as usize..r as usize].chars().rev().collect::<String>();
    let convert_r = &s[r as usize..];

    println!("{}{}{}", convert_l, convert_sub, convert_r);
}
