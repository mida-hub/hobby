# setup
```
rustup toolchain install 1.55.0
rustup default 1.55.0
rustc --version
```

# cargo-compete
```
https://github.com/qryxip/cargo-compete/blob/master/README-ja.md
cargo install cargo-compete --locked
cargo compete init atcoder
cargo compete login atcoder
cargo compete new abc233
# Cargo.toml に 記述する
proconio = "0.4.3"
cargo compete open
cargo run --bin abc233-a < input.txt
cargo compete test a
cargo compete submit a
```
