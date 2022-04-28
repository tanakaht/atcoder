use proconio::input;

fn main() {
    input! {
        n: usize,
        aa: [i32; n], // a is Vec<i32>, n-array.
    }
    let mut stack: Vec<(i32, i32)> = Vec::new();
    let mut ans = 0;
    for a in aa {
        match stack.pop() {
            None => {
                stack.push((a, 1));
            },
            Some((v, mut cnt)) => {
                if v == a {
                    cnt += 1;
                    if cnt<a {
                        stack.push((v, cnt));
                    } else {
                        ans -= a;
                    }
                } else {
                    stack.push((v, cnt));
                    stack.push((a, 1));
                }
            }
        }
        ans += 1;
        println!("{}", ans)
    }
}
