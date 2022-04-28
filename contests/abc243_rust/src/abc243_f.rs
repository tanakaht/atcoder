use proconio::input;
fn main() {
    input! {
        n: usize,
        m: usize,
        k: usize,
        ws: [i32; n] // `a` is Vec<Vec<i32>>, (m, n)-matrix.
    }
    let MOD = 998244353;
    let eleinv = modpow (ws.sum());
    println!("{:?}", ws)
}
