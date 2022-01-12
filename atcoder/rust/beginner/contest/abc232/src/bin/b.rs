use proconio::marker::Bytes;

fn main() {
    proconio::input! {
        s: Bytes,
        t: Bytes,
    }

    let mut diff = 0;
    let mut ans = true; 
    for i in 0..s.len() {
        // println!("{}", (s[i] as isize - t[i] as isize + 26) % 26);
        if i == 0 {
            diff = (s[i] as isize - t[i] as isize + 26) % 26;
        } else if diff != ((s[i] as isize - t[i] as isize + 26) % 26) {
            ans = false;
        }
    }
    if ans {
        println!("Yes");
    } else {
        println!("No");
    }
}
