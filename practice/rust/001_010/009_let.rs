fn main(){
    let immut_val = 10;
    let mut mut_val = 20;

    mut_val += immut_val;
    println!("{}", mut_val);
}
