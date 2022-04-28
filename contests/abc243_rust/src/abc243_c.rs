use std::collections::HashMap;

use proconio::{input, marker::Chars};

fn main() {
    input! {
        n: usize,
        //m: usize,
        //a: [[i32]; n], // a is Vec<i32>, n-array.
        xy: [[i32; 2]; n], // `a` is Vec<Vec<i32>>, (m, n)-matrix.
        s: Chars
    }
    let mut l_d: HashMap<i32, i32> = HashMap::new();
    let mut r_d: HashMap<i32, i32> = HashMap::new();
    for i in 0..n {
        let x = xy[i][0];
        let y = xy[i][1];
        if s[i] == 'L' {
            if !(l_d.contains_key(&y) && l_d[&y] > x){
                l_d.insert(y, x);
            }
        } else {
            if !(r_d.contains_key(&y) && r_d[&y] < x){
                r_d.insert(y, x);
            }
        }
    }
    for (y, x) in l_d.iter(){
        if (r_d.contains_key(y) && r_d[y] < *x){
            println!("Yes");
            return
        }
    }
    println!("No");
}
