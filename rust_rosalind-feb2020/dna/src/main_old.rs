// DNA nucleotide counter in rust

use std::fmt;

#[derive(Debug, Default)]
struct NucleotideCountResult {
    // u32 nums cannot be negative
    a: u32,
    c: u32,
    g: u32,
    t: u32
}

impl fmt::Display for NucleotideCountResult {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{} {} {} {}", self.a, self.c, self.g, self.t)
    }
}

fn main() {
    //makeVar mutable myVarName: typeOfTheVariable = {}
    let dna =
        String::from("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC");

    let mut counter: NucleotideCountResult = Default::default();

    for nucleotide in dna.chars() {
        match nucleotide {
            'A' => counter.a += 1,
            'C' => counter.c += 1,
            'G' => counter.g += 1,
            'T' => counter.t += 1,
            //all possible chars other chars
            _ => ()
        }
    }

    println!("{}", counter);
}
