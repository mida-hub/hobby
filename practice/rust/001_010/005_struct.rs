fn main(){
    #[derive(Debug)]
    struct Person {
        name: String,
        age: u32,
    }

    let p = Person {
        name: String::from("John"),
        age: 33,
    };

    println!("{:?}", p);
}
