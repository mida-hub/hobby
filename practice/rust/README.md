# setup
```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
rustup component add rls rust-analysis rust-src
```

# create project
## web-memory
```
cargo new web-memory
```

## test-futures
```
cargo new test-futures
cargo add futures
```

# build & run
コンパイル
```
cargo build
```

コンパイル&実行
```
cargo run
```
