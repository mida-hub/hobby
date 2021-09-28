struct Droppable;

impl Drop for Droppable {
    fn drop(&mut self){
        println!("Resource will be released!");
    }
}

fn main(){
    println!("Start");
    {
        let d = Droppable;
        println!("Doing");
    }
    println!("The Droppable should be relased at the end of block.");
}
