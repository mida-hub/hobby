fn main(){
    let mut v1 = vec![1, 2, 3, 4, 5];
    let v2 = vec![0; 5];
    println!("{:?}", v1);
    println!("{:?}", v2);
    v1[1] = 0;
    println!("{:?}", v1);

    for element in &v1{
        println!("{}", element);
    }
}
