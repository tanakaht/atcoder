use proconio::input;

fn main() {
    input! {
        a: usize,
        b: usize,
        c: usize,
        x: usize,
        //m: usize,
        //a: [[i32]; n], // a is Vec<i32>, n-array.
        //ab: [[i32; n]; m] // `a` is Vec<Vec<i32>>, (m, n)-matrix.
    }
    if x<=a{
        println!("{}", 1)
    } else if x<=b {
        println!("{}", (c as f32)/((b-a) as f32))
    } else{
        println!("{}", 0)
    }
}
