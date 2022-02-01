use proconio::input;

fn main() {
    input! {
        x: i32,
        y: i32,
    }
    let mut ans = std::cmp::max(0, (y-x)/10);
    if (y-x)%10!=0 && (y-x)>= 0{
        ans += 1
    }
    println!("{}", ans);
}
