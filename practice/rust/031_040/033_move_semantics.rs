struct Color {
    r: i32,
    g: i32,
    b: i32,
}

fn main(){
    let a = Color{r:255, g:155, b:55};
    let b = a;
    println!("{} {} {}", b.r, b.g, b.b);
}
