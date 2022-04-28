use proconio::input;

fn main() {
    input! {
        mut v: i64,
        a: i64,
        b: i64,
        c: i64,
    }
    v %= (a+b+c);
    v -= a;
    if v < 0 {
        println!("F");
        return
    }
    v -= b;
    if v<0 {
        println!("M");
        return
    }
    v -= c;
    if v<0 {
        println!("T");
        return
    }
}
