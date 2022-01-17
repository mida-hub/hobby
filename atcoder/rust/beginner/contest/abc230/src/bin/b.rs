fn main() {
    proconio::input! {
        s: String,
    }

    let s_len = s.len();
    // 1文字はYes
    if s_len == 1 {
        println!("Yes");
        return
    }

    // 2文字でooはNo
    if s_len == 2 && s == "oo" {
        println!("No");
        return
    }

    // 2文字でooでなければYes
    if s_len == 2 {
        println!("Yes");
        return
    }

    // 先頭3文字が下記パターン以外はNo
    let patterns = ["oxx", "xxo", "xox"];
    let s_substr = &s[..3];

    if !patterns.contains(&s_substr) {
        println!("No");
        return
    }

    // oxx のパターンをサーチするために初期位置を決定する
    let start_index;
    if s_substr == "oxx" {
        start_index = 0;
    } else if s_substr == "xox" {
        start_index = 1;
    } else {
        start_index = 2;
    }
    
    for i in start_index..s_len {
        if (i - start_index) % 3 == 0 {
            if s.chars().nth(i).unwrap().to_string() != "o" {
                println!("No");
                return
            } 
        }

        if (i - start_index) % 3 == 1 {
            if s.chars().nth(i).unwrap().to_string() != "x" {
                println!("No");
                return
            } 
        }

        if (i - start_index) % 3 == 2 {
            if s.chars().nth(i).unwrap().to_string() != "x" {
                println!("No");
                return
            } 
        }
    }
    println!("Yes");
}
