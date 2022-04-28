use proconio::input;

fn bisect(n: usize, k1: usize, k2: usize, k3: usize) -> usize {
    if k3 >= n {
        return 0
    }
    let mut ok: usize = 1000000;
    let mut ng: usize = 0;
    while (ok-ng) > 1{
        let mid = (ok+ng)/2;
        if (mid.pow(3)+k1*mid.pow(2)+k2*mid+k3)>=n{
            ok = mid;
        } else {
            ng = mid;
        }
    }
    return ok
}

fn main() {
    input! {
        n: usize,
    }
    let mut ans: usize = 1000000000000000000;
    for b in 0..1000000{
        let a = bisect(n, b, b*b, b*b*b);
        let x = a*a*a + a*a*b + a*b*b + b*b*b;
        if x<ans {
            ans = x
        }
    }
    println!("{}", ans)
}
