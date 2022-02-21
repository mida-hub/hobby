// abc232c
use itertools::Itertools;

fn main() {
    proconio::input! {
        n: usize,
        m: usize,
        ab: [[usize; 2]; m],
        cd: [[usize; 2]; m],
    }

    // println!("{},{}", n, m);
    // println!("{:?}", ab);
    // println!("{:?}", cd);

    // ボールの対応表を作成
    let mut ab_matrix = vec![vec![false; n]; n];
    let mut cd_matrix = vec![vec![false; n]; n];

    for abi in &ab {
        let ai = abi[0] - 1;
        let bi = abi[1] - 1;
        ab_matrix[ai][bi] = true;
        ab_matrix[bi][ai] = true;
    }
    // println!("{:?}", ab_matrix);

    for cdi in &cd {
        let ci = cdi[0] - 1;
        let di = cdi[1] - 1;
        cd_matrix[ci][di] = true;
        cd_matrix[di][ci] = true;
    }
    // println!("{:?}", cd_matrix);

    for perm in (0..n).permutations(n) {
        // println!("{:?}", perm);

        let mut ans = true;
        for i in 0..n {
            for j in 0..n {
                // println!("i,j,perm[i],perm[j]:{},{},{},{}={}", i+1, j+1, perm[i]+1, perm[j]+1, ab_matrix[i][j] == cd_matrix[perm[i]][perm[j]]);
                if ab_matrix[i][j] != cd_matrix[perm[i]][perm[j]] {
                    ans = false;
                }
            }
        }
        if ans {
            // println!("{:?}", perm);
            println!("Yes");
            return
        }
    }
    println!("No");
}
