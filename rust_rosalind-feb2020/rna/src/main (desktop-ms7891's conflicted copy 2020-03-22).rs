use std::io::{self, BufRead};

fn main() {
    // terminal input
    let mut _dna = String::new();
    let stdin = io::stdin();
    stdin.lock().read_line(&mut _dna).expect("Could not read line");

    // Sample DataSet
    // let _dna = String::from("GATGGAACTTGACTACGTAAATT");

    let mut _rna = String::from("");

    for nucleotide in _dna.chars() {
        match nucleotide {
            'A' => _rna.push_str("A"),
            'C' => _rna.push_str("C"),
            'G' => _rna.push_str("G"),
            'T' => _rna.push_str("U"),
            _ => ()
        }
    }

    println!("{}", _rna);
}
