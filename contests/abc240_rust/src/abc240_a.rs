use proconio::input;

fn main() {
    input! {
        a: i32,
        b: i32,
        //m: usize,
        //a: [[i32]; n], // a is Vec<i32>, n-array.
        //ab: [[i32; n]; m] // `a` is Vec<Vec<i32>>, (m, n)-matrix.
    }
    let ans: &str;
    if (b-a).abs()==1 {
        ans = "Yes"
    } else if b==10 && a==1 {

        ans = "Yes"
    } else {
        ans = "No"
    }
    println!("{}", ans)
}
