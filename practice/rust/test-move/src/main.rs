use futures::executor;
use futures::future::Future;

fn move_to_async_block() -> impl Future<Output = ()> {
    let outside_variable = "this is outside".to_string();
    async move {
        println!("{}", outside_variable);
    }
}

fn main(){
    executor::block_on(move_to_async_block());
}
