use proconio::input;

fn main() {
    input! {
        a: f64,
        b: f64,
        //m: usize,
        //a: [[i32]; n], // a is Vec<i32>, n-array.
        //ab: [[i32; n]; m] // `a` is Vec<Vec<i32>>, (m, n)-matrix.
    }
    if a==0.0 {
        println!("0 1",)
    } else {
        let d = (a*a+b*b).sqrt();
        println!("{} {}", a/d, b/d);
    }
}
