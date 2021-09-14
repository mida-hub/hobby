use hyper::service::{make_service_fn, service_fn};
use hyper::{Body, Error, Request, Response, Server};
use hyper::Method;
use std::str;
use std::{convert::Infallible, net::SocketAddr};
use tera::{Context, Tera};
use std::sync::Arc;
use serde::Deserialize;
use uuid::Uuid;
use rusqlite::{params, Connection};
use tokio::sync::Mutex;

static TEMPLATE: &str = "Hello, {{name}}!";

#[derive(Deserialize)]
struct NewPost<'a>{
    title: &'a str,
    content: &'a str,
}

async fn create_post(
        req: Request<Body>,
        _: Arc<Tera>,
        conn: Arc<Mutex<Connection>>,
    )->Result<Response<Body>, Error>{
    let body = hyper::body::to_bytes(req.into_body()).await?;
    let new_post = serde_urlencoded::from_bytes::<NewPost>(&body).unwrap();
    let id = Uuid::new_v4();

    conn.lock()
        .await
        .execute(
            "INSERT INTO posts(id, title, content) VALUES (?1, ?2, ?3)",
            params![&id, new_post.title, new_post.content],
        )
        .unwrap();

    Ok(Response::new(id.to_string().into()))
}

async fn handle(_: Request<Body>)-> Result<Response<Body>, Infallible>{
    Ok(Response::new("Hello, World!".into()))
}

async fn handle_with_body(req: Request<Body>, tera: Arc<Tera>)->Result<Response<Body>, Error>{
    let body = hyper::body::to_bytes(req.into_body()).await?;

    let body = str::from_utf8(&body).unwrap();
    let name = body.strip_prefix("name=").unwrap();

    let mut ctx = Context::new();
    ctx.insert("name", name);
    let rendered = tera.render("hello", &ctx).unwrap();

    Ok(Response::new(rendered.into()))
}

async fn route(req: Request<Body>, tera: Arc<Tera>)->Result<Response<Body>, Error>{
    match *req.method(){
        Method::POST => handle_with_body(req, tera).await,
        _ => handle(req).await.map_err(|e| match e {})
    }
}

#[tokio::main]
async fn main() {
    let addr = SocketAddr::from(([127,0,0,1], 3000));

    let mut tera = Tera::default();
    tera.add_raw_template("hello", TEMPLATE).unwrap();
    let tera = Arc::new(tera);

    let make_svc = make_service_fn(|_conn| {
        let tera = tera.clone();
        async {
            Ok::<_, Infallible>(service_fn(move |req|{
                route(req, tera.clone())
            }))
        }
    });

    let server = Server::bind(&addr).serve(make_svc);

    if let Err(e) = server.await {
        eprintln!("server error: {}", e);
    }
}
