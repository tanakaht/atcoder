use proconio::input;
use std::collections::HashSet;

fn main() {
    input! {
        n: usize,
        a: [i32; n], // a is Vec<i32>, n-array.
    }
    let s: HashSet<i32> = a.into_iter().collect();
    println!("{}", s.len())
}
