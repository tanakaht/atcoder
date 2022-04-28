use proconio::{input, marker::Chars};


fn get_bitlength(v: usize) -> usize {
    if v==0{
        return 1
    }
    let mut ret = 0;
    let mut tmp = v;
    while tmp>0 {
        ret += 1;
        tmp /= 2;
    }
    return ret
}

fn nthchar(t:usize, k:usize) -> usize {
    let mut i = 0;
    let mut l = 1;
    while i < t && l<k {
        l *= 2;
        i += 1;
    }
    if i!=t || k==0 {
        return 0
    } else {
        return k/l
    }
}

fn solve(c: char, t: usize, k: usize) -> char {
    let abc = vec!['A', 'B', 'C'];
    let mut idx: usize;
    if c=='A' {
        idx = 0
    } else if c=='B' {
        idx = 1
    } else {
        idx = 2
    }
    let popcount = k.count_ones() as usize;
    let bitlength = get_bitlength(k);
    // idx = (idx+1)%3;
    idx = (idx+(bitlength-1)+popcount)%3;
    idx = (idx+t-(bitlength-1))%3;
    return abc[idx]
}

fn main() {
    input! {
        s: Chars,
        q: usize,
        tk: [[usize; 2]; q] // `a` is Vec<Vec<i32>>, (m, n)-matrix.
    }
    for ele in tk {
        let t = ele[0];
        let mut k = ele[1]-1;
        let cidx = nthchar(t, k);
        if cidx != 0 {
            k -= 2usize.pow(t as u32)*cidx
        }
        println!("{}", solve(s[cidx], t, k))
    }
}
