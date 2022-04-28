use proconio::{input, marker::Chars};

fn main() {
    input! {
        mut s: Chars,
        //m: usize,
        //a: [[i32]; n], // a is Vec<i32>, n-array.
        //ab: [[i32; n]; m] // `a` is Vec<Vec<i32>>, (m, n)-matrix.
    }
    s.sort();
    let ans: String = s.iter().collect();
    println!("{}", ans)
}
