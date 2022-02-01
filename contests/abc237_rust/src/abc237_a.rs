use proconio::input;

fn main() {
    input! {
        n: i64,
    }
    if n < -(1<<31) {
        println!("{}", "No");
    } else if n >= (1<<31) {
        println!("{}", "No");
    } else {
        println!("{}", "Yes");
    }
}
