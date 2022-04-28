use proconio::input;

fn main() {
    input! {
        n: usize,
        m: usize,
        abc: [[usize; 3]; m] // `a` is Vec<Vec<i32>>, (m, n)-matrix.
    }
    let mut g: Vec<Vec<(usize, usize)>> = vec![Vec::new(); n];
    let mut dist = vec![vec![std::usize::MAX/4; n]; n];
    for i in 0..n {
        dist[i][i] = 0;
    }
    for ele in abc {
        let u = ele[0];
        let v = ele[1];
        let c = ele[2];
        g[u-1].push((v-1, c));
        g[v-1].push((u-1, c));
        dist[u-1][v-1] = c;
        dist[v-1][u-1] = c;
    }
    for k in 0..n {
        for i in 0..n {
            for j in 0..n {
                if dist[i][j] > dist[i][k] + dist[k][j]{
                    dist[i][j] = dist[i][k] + dist[k][j]
                }
            }
        }
    }
    let mut ans = 0;
    for i in 0..n {
        for (j, c) in g[i].iter() {
            for k in 0..n{
                if k!=i && k!=*j && *c >= dist[i][k] + dist[k][*j]{
                    ans += 1;
                    break
                }
            }

        }
    }
    println!("{}", ans/2)
}
