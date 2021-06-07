fn main(){
    let a: [i32; 3] = [0, 1, 2];
    let b: [i32; 3] = [0; 3];
    println!("{:?}", a);
    println!("{:?}", b);
    println!("{:?}", a[1]);
    println!("{:?}", &a[1..3]);
}
