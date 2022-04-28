use proconio::input;
use std::collections::HashSet;

fn main() {
    input! {
        n: usize,
        x: i32,
        ab: [[i32; 2]; n] // `a` is Vec<Vec<i32>>, (m, n)-matrix.
    }
    let mut available: HashSet<i32> = HashSet::new();
    let mut new_available: HashSet<i32> = HashSet::new();
    available.insert(0);
    for i in 0..n {
        let a = ab[i][0];
        let b = ab[i][1];
        for v in available {
            if v+a<=x {
                new_available.insert(v+a);
            }
            if v+b<=x {
                new_available.insert(v+b);
            }
        }
        available = new_available;
        new_available = HashSet::new();
    }
    if available.contains(&x){
        println!("{}", "Yes")
    } else {
        println!("{}", "No")
    }
}
