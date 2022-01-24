fn main() {
    proconio::input! {
        s: usize,
    mut t: usize,
    mut x: usize,
    }

    if t < s {
        t = t + 24;
    }
    if x < s {
        x = x + 24;
    }

    if s <= x && x < t {
        println!("Yes");
    } else {
        println!("No");
    }
}
