use proconio::{input, marker::Chars};

fn main() {
    input! {
        t: usize,
    }
    // A =65
    let MOD =998244353;
    for _ in 0..t {
        input! {
            n: usize,
            s: Chars
        }
        let mut cnt = 0;
        let mut s2: Vec<char> = Vec::new();
        for i in 0..(n+1)/2 {
            cnt = (cnt*26+(s[i] as i64)-65)%MOD;
            s2.push(s[i]);
        }
        let mut tmp = s2.to_vec();
        if n%2==1 {
            tmp.pop();
        }
        tmp.reverse();
        s2.append(&mut tmp);
        if s >= s2 {
            cnt += 1
        }
        println!("{}", cnt%MOD);
    }
}
