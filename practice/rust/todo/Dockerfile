FROM rust:1.52 AS builder

WORKDIR /todo
COPY Cargo.toml Cargo.toml

# ビルドするために何もしないソースコードを入れておく
RUN mkdir src
RUN echo "fn main(){}" > src/main.rs

# パッケージ分だけコンパイルされる
RUN cargo build --release

# 改めてソースコードを投入する
COPY ./src ./src
COPY ./templates ./templates

# アプリケーションに関わるものを削除する
RUN rm -f target/release/deps/todo*
RUN cargo build --release

FROM debian:10.4

COPY --from=builder /todo/target/release/todo /usr/local/bin/todo

ENTRYPOINT ["todo"]
