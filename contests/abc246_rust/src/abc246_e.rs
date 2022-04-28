use std::collections::BinaryHeap;
use proconio::{input, marker::Chars};
const INF: usize = 1000000000;
fn main() {
    input! {
        n: usize,
        ax: usize,
        ay: usize,
        bx: usize,
        by: usize,
        S: [Chars; n] // `a` is Vec<Vec<i32>>, (m, n)-matrix.
    }
    let mut dist: Vec<Vec<usize>> = vec![vec![INF; n]; n];
    let mut appeared: Vec<Vec<bool>> = vec![vec![false; n]; n];
    let mut appearedd14: Vec<Vec<bool>> = vec![vec![false; n]; n];
    let mut appearedd23: Vec<Vec<bool>> = vec![vec![false; n]; n];
    let mut q: BinaryHeap<(i64, usize, usize)> = std::collections::BinaryHeap::new();
    q.push((0, ax-1, ay-1));
    dist[ax-1][ay-1] = 0;
    while !q.is_empty(){
        let (di64, x, y) = q.pop().unwrap();
        let d = di64.abs() as usize;
        if appeared[x][y]{
            continue;
        }
        appeared[x][y] = true;
        if !appearedd14[x][y]{
            for nume in [-1, 1].iter(){
                for step in 1..n{
                    let mut x_ = x;
                    let mut y_ = y;
                    if *nume==-1{
                        if (x<step || y<step) {
                            break
                        }
                        x_ -= step;
                        y_ -= step;
                    } else {
                        x_ += step;
                        y_ += step;
                    }
                    if x_>=n || y_>=n {
                        break
                    } else if S[x_][y_]=='#' {
                        break
                    } else if dist[x_][y_] > d+1 {
                        dist[x_][y_] = d+1;
                        q.push(((-1)*((d+1) as i64), x_, y_));
                        appearedd14[x_][y_] = true;
                    }
                }
            }
        }
        if !appearedd23[x][y]{
            for nume in [-1, 1].iter(){
                for step in 1..n{
                    let mut x_ = x;
                    let mut y_ = y;
                    if *nume==-1{
                        if (x<step) {
                            break
                        }
                        x_ -= step;
                        y_ += step;
                    } else {
                        if (y<step) {
                            break
                        }
                        x_ += step;
                        y_ -= step;
                    }
                    if x_>=n || y_>=n {
                        break
                    } else if S[x_][y_]=='#' {
                        break
                    } else if dist[x_][y_] > d+1 {
                        dist[x_][y_] = d+1;
                        q.push(((-1)*((d+1) as i64), x_, y_));
                        appearedd23[x_][y_] = true;
                    }
                }
            }
        }
    }
    let ans = dist[bx-1][by-1];
    if ans == INF {
        println!("-1");
    } else {
        println!("{}", ans);
    }
}
