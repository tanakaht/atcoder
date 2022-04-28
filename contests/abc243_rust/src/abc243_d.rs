use proconio::{input, marker::Chars};

fn main() {
    input! {
        n: usize,
        mut x: usize,
        s: Chars,
        //m: usize,
        //a: [[i32]; n], // a is Vec<i32>, n-array.
        //ab: [[i32; n]; m] // `a` is Vec<Vec<i32>>, (m, n)-matrix.
    }
    let mut s_filtered: Vec<char> = Vec::new();
    for i in 0..n {
        if s[i] == 'U'{
            let ele = s_filtered.pop();
            match ele {
                None => s_filtered.push(s[i]),
                Some('U') => {
                    s_filtered.push('U');
                    s_filtered.push(s[i]);
                },
                _ => (),
            }
        } else {
            s_filtered.push(s[i])
        }
    }
    for c in s_filtered{
        match c {
            'U' => x = x/2,
            'L' => x = x*2,
            'R' => x = x*2+1,
            _ => ()
        }
    }
    println!("{}", x)
}
