use futures::executor;
use futures::future::Future;

async fn async_add(left: i32, right: i32) -> i32 {
    left + right
}

async fn something_great_async_function_1() -> i32 {
    let ans = async_add(2, 3).await;
    println!("fn1={}", ans);
    ans
}

fn something_great_async_function_2() -> impl Future<Output = i32> {
    async {
        let ans = async_add(2, 3).await;
        println!("fn2={}", ans);
        ans
    }
}

fn main(){
    executor::block_on(something_great_async_function_1());
    executor::block_on(something_great_async_function_2());
}
