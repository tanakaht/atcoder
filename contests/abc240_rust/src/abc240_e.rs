use proconio::input;
use std::collections::HashMap;

fn main() {
    input! {
        n: usize,
        uv: [(usize, usize); n-1] // `a` is Vec<Vec<i32>>, (m, n)-matrix.
    }
    let mut g: Vec<Vec<usize>> = vec![Vec::new(); n];
    let mut children: Vec<Vec<usize>> = vec![Vec::new(); n];
    let mut parents= vec![n; n];
    for (u, v) in uv {
        g[u-1].push(v-1);
        g[v-1].push(u-1);
    }
    let mut stack: Vec<(usize, usize)> = vec![(0, n)];
    while stack.len()>0 {
        let (u, p) = stack.pop().unwrap();
        for v in g.get(u).unwrap() {
            if *v != p {
                parents[*v] = u;
                children[u].push(*v);
                stack.push((*v, u));
            }
        }
    }
    let mut memo: HashMap<usize, i32> = HashMap::new();
    fn child_cnt(u: usize, children: &mut Vec<Vec<usize>>,memo: &mut HashMap<usize, i32>) -> i32{
        return match memo.get(&u) {
            None => {
                let mut ret: i32 = 1;
                let mut childs: Vec<usize> = Vec::new();
                for v in children.get(u).unwrap() {
                    childs.push(*v);
                }
                if childs.len() != 0 {
                    ret -= 1;
                }
                for v in childs {
                    ret += child_cnt(v, children, memo);
                }
                memo.insert(u, ret);
                return ret
            }
            _ => memo[&u]
        }
    }
    let mut anss: HashMap<usize, (i32, i32)> = HashMap::new();
    let mut stack: Vec<usize> = Vec::new();
    anss.insert(0, (0, child_cnt(0, &mut children, &mut memo)));
    stack.push(0);
    while stack.len()>0 {
        let u = stack.pop().unwrap();
        let (l, _) = anss.get(&u).unwrap();
        let mut p = *l;
        let mut childs: Vec<usize> = Vec::new();
        {
            for v in children.get(u).unwrap() {
                childs.push(*v);
            }
        }
        for v in childs{
            let cnt = child_cnt(v, &mut children, &mut memo);
            anss.insert(v, (p, p+cnt));
            p += cnt;
            stack.push(v);
        }
    }
    for u in 0..n{
        let (l, r)= anss.get(&u).unwrap();
        println!("{} {}", l+1, r);
    }
}
