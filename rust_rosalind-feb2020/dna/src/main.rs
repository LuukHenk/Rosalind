use std::io::{self, BufRead, Error, ErrorKind, Read, Seek, SeekFrom};
use std::fmt;
use std::fs;
use std::path::Path;

const BUF_SIZE: usize = 100000;
const USER_INP: bool = false;

#[derive(Debug, Default)]
struct NucleotideCountResult {
    // u32 nums cannot be negative
    a: u32,
    c: u32,
    g: u32,
    t: u32
}

fn user_input() -> String {
    let mut inp = String::new();
    let stdin = io::stdin();
    stdin.lock().read_line(&mut inp).expect("Could not read line");

    inp
}

impl fmt::Display for NucleotideCountResult {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{} {} {} {}", self.a, self.c, self.g, self.t)
    }
}

fn main() -> io::Result<()> {
    // Buf size must have at least a size of 1
    if BUF_SIZE < 1 {
        let invalid_bufsize_error = Error::new(ErrorKind::InvalidInput,
                                               "BUF_SIZE must have at least a value of 2");
        eprintln!("{:?}", invalid_bufsize_error);
        std::process::exit(1);
    }

    // let mut loading_path = Path::new("./sample_dataset.txt").to_path_buf();
    let mut loading_path = Path::new("./rosalind_dna.txt").to_path_buf();
    if USER_INP {
        while loading_path.pop() {};
        println!("Please enter a file path:");
        loading_path.push(user_input().trim());
    }

    if loading_path.exists() {
        let mut f = fs::File::open(loading_path)?;

        let mut dna = vec![1; BUF_SIZE];

        let mut counter: NucleotideCountResult = Default::default();

        let mut offset = 0;
        let mut enter_found = false;

        f.seek(SeekFrom::Start(offset))?;
        let _bytes = f.read(&mut dna)?;

        loop {
            f.seek(SeekFrom::Start(offset))?;
            let _bytes = f.read(&mut dna)?;

            for nucleotide in &dna {
                match nucleotide {
                    b'A' => counter.a += 1,
                    b'C' => counter.c += 1,
                    b'G' => counter.g += 1,
                    b'T' => counter.t += 1,
                    b'\n' => enter_found = true,
                    //all possible chars other chars
                    _ => ()
                }
                println!("{:?} {}", enter_found, nucleotide);

                if enter_found {
                    break;
                }
            }

            if enter_found {
                println!("{}", counter);
                break;
            } else {
                    offset += BUF_SIZE as u64;
            }
        }

    } else {
        println!("Path '{:?}' cannot be found!", loading_path);
    }
    Ok(())
}
