use std::collections::{HashSet, HashMap};

use proconio::input;

fn main() {
    input! {
        xys: [[isize; 2]; 3]
        //m: usize,
        //a: [[i32]; n], // a is Vec<i32>, n-array.
        //ab: [[i32; n]; m] // `a` is Vec<Vec<i32>>, (m, n)-matrix.
    }
    let x1 = xys[0][0];
    let y1 = xys[0][1];
    let x2 = xys[1][0];
    let y2 = xys[1][1];
    let x3 = xys[2][0];
    let y3 = xys[2][1];
    let mut availables: HashSet<(isize, isize)> = HashSet::new();
    for x in [x1, x2, x3].iter() {
        for y in [y1, y2, y3].iter() {
            availables.insert((*x, *y));
        }
    }
    for (x, y) in [(x1, y1), (x2, y2), (x3, y3)].iter() {
        availables.remove(&(*x, *y));
    }
    for (x, y) in availables{
        println!("{} {}", x, y)
    }
}
