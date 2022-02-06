use std::io::{self, BufRead};

fn main() {
    let mut _dna = String::new();
    let stdin = io::stdin();
    stdin.lock().read_line(&mut _dna).expect("Could not read line");

    // Sample DataSet
    // let _dna = String::from("AAAACCCGGT");

    let _dna_reverse =  _dna.chars().rev().collect::<String>();

    let mut _complement = String::from("");
    for nucleotide in _dna_reverse.chars() {
        match nucleotide {
            'A' => _complement.push_str("T"),
            'C' => _complement.push_str("G"),
            'G' => _complement.push_str("C"),
            'T' => _complement.push_str("A"),
            _ => ()
        }
    }

    println!("{}", _complement);

}
