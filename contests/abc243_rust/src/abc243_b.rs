use std::collections::HashSet;

use proconio::input;

fn main() {
    input! {
        n: usize,
        //m: usize,
        a: [i32; n], // a is Vec<i32>, n-array.
        b: [i32; n], // a is Vec<i32>, n-array.
        //ab: [[i32; n]; m] // `a` is Vec<Vec<i32>>, (m, n)-matrix.
    }
    let mut cnt1 = 0;
    let mut cnt2 = 0;
    for i in 0..n {
        for j in 0..n{
            if a[i]==b[j]{
                if i==j {
                    cnt1 += 1
                } else {
                    cnt2 += 1
                }
            }
        }
    }
    println!("{}", cnt1);
    println!("{}", cnt2);
}
