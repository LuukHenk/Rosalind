use std::io::{self, BufRead};

fn main() {
    // terminal input
    let mut dna = String::new();
    let stdin = io::stdin();
    stdin.lock().read_line(&mut dna).expect("Could not read line");

    // Sample DataSet
    // let _dna = String::from("GATGGAACTTGACTACGTAAATT");

    let mut rna = String::from("");

    for nucleotide in dna.chars() {
        match nucleotide {
            'A' => rna.push_str("A"),
            'C' => rna.push_str("C"),
            'G' => rna.push_str("G"),
            'T' => rna.push_str("U"),
            _ => ()
        }
    }

    println!("{}", rna);
}
