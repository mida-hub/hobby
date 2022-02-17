// abc231c
// https://moshg.github.io/rust-std-ja/std/primitive.slice.html#method.binary_search
fn main() {
    proconio::input! {
        n: usize,
        q: usize,
    mut an: [usize; n],
        xq: [usize; q],
    }
    an.sort();
    // println!("{}, {}", n, q);
    // println!("{:?}", an);
    // println!("{:?}", xq);

    for x in xq {
        // println!("{}", x);
        if an.binary_search(&x).is_ok(){
            println!("{:?}", n - an.binary_search(&x).unwrap());
        } else {
            println!("{:?}", n - an.binary_search(&x).unwrap_err());
        }
    }
}
