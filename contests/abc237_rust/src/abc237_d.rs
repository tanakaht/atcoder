use proconio::marker::Chars;
use proconio::input;
struct  Node{
    l: Option<Box<Node>>,
    r: Option<Box<Node>>,
    i: usize
}

impl Node {
    fn ins_l(&self, elem: usize) -> Node {
        Node {l: self.l, r: Some(Box::new(self)), i:elem}
    }
    fn ins_r(&self, elem: usize) -> Node {
        Node {l: Some(Box::new(*self)), r: self.r, i:elem}
    }
}


fn main() {
    input! {
        n: usize,
        s: [char; n],
    }
    let mut cur: Node = Node {l: None, r: None, i: 0};
    for (i, val) in s.iter().enumerate() {
        match val {
            'L' => {cur = cur.ins_l(i)},
            'R' => {cur = cur.ins_r(i)},
            _ => ()
        }
    }
    println!("{}", n)
}
