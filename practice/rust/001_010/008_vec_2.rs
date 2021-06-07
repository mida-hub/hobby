fn main(){
    let byte_array = [b'h', b'e', b'1'];
    print(Box::new(byte_array));
}

fn print(s: Box<[u8]>){
    println!("{:?}", s);
}
