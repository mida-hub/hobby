use async_trait::async_trait;

struct Human {}
struct Dog {}

#[async_trait]
trait Mammals {
    async fn say_greeting(&mut self);
}

#[async_trait]
impl Mammals for Human {
    async fn say_greeting(&mut self){
        println!("Hello")
    }
}

#[async_trait]
impl Mammals for Dog {
    async fn say_greeting(&mut self){
        println!("Bowwow")
    }
}

#[async_std::main]
async fn main() {
    println!("Hello, world!");

    let mut human = Human{};
    human.say_greeting().await;

    let mut dog = Dog{};
    dog.say_greeting().await;

}
