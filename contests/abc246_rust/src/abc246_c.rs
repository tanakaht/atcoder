use proconio::input;

fn main() {
    input! {
        n: usize,
        k: usize,
        x: usize,
        A: [usize; n], // a is Vec<i32>, n-array.
        //ab: [[i32; n]; m] // `a` is Vec<Vec<i32>>, (m, n)-matrix.
    }
    let mut rests: Vec<usize> = Vec::new();
    let mut cnt: usize = 0;
    for a in A.iter() {
        rests.push(*a%x);
        cnt += *a/x;
    }
    if cnt>=k {
        println!("{}", A.iter().fold(0, |sum, a| sum + a)-k*x);
    } else {
        let mut ans = A.iter().fold(0, |sum, a| sum + a)-cnt*x;
        rests.sort();
        for (i, a) in rests.iter().rev().enumerate(){
            ans -= a;
            if i == k-cnt-1{
                break
            }
        }
        println!("{}", ans);
    }
}
