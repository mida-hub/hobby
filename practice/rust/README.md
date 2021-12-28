# setup
```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
rustup component add rls rust-analysis rust-src
```

# new edition 2021
```
rustup default nightly && rustup update
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

# web assembly
```
cargo install cargo-generate
cargo generate --git https://github.com/rustwasm/wasm-pack-template
-> mandelbrot
curl https://rustwasm.github.io/wasm-pack/installer/init.sh -sSf | sh
cd mandelbrot
wasm-pack build
npm init wasm-app www
cd www
npm install
npm run start
```
