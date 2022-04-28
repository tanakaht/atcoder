use proconio::input;

fn main() {
    input! {
        n: usize,
        //m: usize,
        //a: [[usize]; n], // a is Vec<usize>, n-array.
        //ab: [[usize; n]; m] // `a` is Vec<Vec<usize>>, (m, n)-matrix.
    }
    let mut dp: Vec<Vec<usize>> = vec![vec![0; 11]; n];
    let MOD = 998244353;
    for i in 1..10 {
        dp[0][i] = 1;
    }
    for i in 1..n {
        for j in 1..10 {
            dp[i][j] = (dp[i-1][j-1]+dp[i-1][j]+dp[i-1][j+1])%MOD
        }
    }
    let mut ans = 0;
    for j in 1..10 {
        ans = (ans+dp[n-1][j])%MOD
    }
    println!("{}", ans);
}
