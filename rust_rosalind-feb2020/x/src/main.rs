use std::fs;

fn main() {
    let loading_path = "/home/zoutekaas/Dropbox/home/sid/rosalind/input/rosalind_rna.txt";
    let data = fs::read_to_string(loading_path).expect("Unable to read file");
    println!("{}", data);
}
