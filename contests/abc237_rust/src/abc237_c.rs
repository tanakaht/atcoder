use proconio::input;

fn main() {
    input! {
        s: String,
    }
    let slice = s.chars().collect::<Vec<char>>();
    let mut l = 0;
    let mut r = s.len()-1;
    while l<s.len() && slice[l] == 'a'{
        l += 1;
    }
    while r>l && slice[r] == 'a'{
        r -= 1;
    }
    let mut flg: bool = true;
    if l>=r {
    } else if s.len()-r-1 < l {
        flg = false
    } else if r>l {
        for i in 0..(r-l) {
            flg = flg && slice[l+i]==slice[r-i];
        }
    }
    if flg {
        println!("Yes")
    } else {
        println!("No")
    }
}
