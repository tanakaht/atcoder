use proconio::input;

fn main() {
    input! {
        x: i32,
        y: i32,
    }
    println!("{}", (y-x)/10+1);
}
