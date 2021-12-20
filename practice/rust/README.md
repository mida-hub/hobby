# setup
```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
rustup component add rls rust-analysis rust-src
```

# create project
```
cargo new test-futures
cargo add futures
```

# create crate
```
cargo new --lib new_crate
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

# error handle
```
cargo add anyhow
cargo add thiserror
```
