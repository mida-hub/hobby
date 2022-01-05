use proconio::input;

fn main() {
    input! {
        x: i32,
        y: i32,
    }
    let y_x = y - x;

    if y_x <= 0 {
        println!("0");
    } else {
        let remain = (y_x as f32 / 10.0).ceil();
        println!("{}", remain);
    }
}
