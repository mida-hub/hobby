fn main() {
    proconio::input! {
        s1: String,
        s2: String,
    }
    let s11 = s1.chars().nth(0).unwrap();
    let s12 = s1.chars().nth(1).unwrap();
    let s21 = s2.chars().nth(0).unwrap();
    let s22 = s2.chars().nth(1).unwrap();

    let mut ans = true;
    if s11 == '#' && s12 == '.' && s21 == '.' {
        ans = false;
    }
    if s12 == '#' && s11 == '.' && s22 == '.' {
        ans = false;
    }
    if s21 == '#' && s11 == '.' && s22 == '.' {
        ans = false;
    }
    if s22 == '#' && s12 == '.' && s21 == '.' {
        ans = false;
    }

    if ans {
        println!("Yes");
    } else {
        println!("No");
    }
}
