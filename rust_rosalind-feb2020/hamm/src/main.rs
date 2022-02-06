use std::io::{self, Read, Seek, SeekFrom, BufRead, Error, ErrorKind};
use std::fs;
use std::path::Path;

const BUF_SIZE: usize = 100000;
const USER_INP: bool = false;

fn offset_of_first(char_byte: u8, file: &mut fs::File) -> usize {
    let mut offset = 0;
    let mut buf = [1; BUF_SIZE];

    loop {
        let bytes = file.read(&mut buf).expect("Failed to read into buffer");

        match buf.iter().position(|&byte| byte == char_byte) {
            Some(n) => {
                offset += n;
                break;
            },
            None => {
                if bytes < buf.len() {
                    break;
                } else {
                    offset += bytes;
                }
            }
        }
    }

    offset
}

fn user_input() -> String {
    let mut inp = String::new();
    let stdin = io::stdin();
    stdin.lock().read_line(&mut inp).expect("Could not read line");

    inp
}

fn main() -> io::Result<()> {
    // Buf size must have at least a size of 2
    if BUF_SIZE < 2 {
        let invalid_bufsize_error = Error::new(ErrorKind::InvalidInput,
                                               "BUF_SIZE must have at least a value of 2");
        eprintln!("{:?}", invalid_bufsize_error);
        std::process::exit(1);
    }

    let mut loading_path = Path::new("./rosalind_hamm.txt").to_path_buf();
    if USER_INP {
        while loading_path.pop() {};
        println!("Please enter a file path:");
        loading_path.push(user_input().trim());
    }

    if loading_path.exists() {
        let mut f = fs::File::open(loading_path)?;

        let enter_offset = offset_of_first(b'\n', &mut f);
        let enter_offset_64 = enter_offset as u64;

        let strand_buf_size = BUF_SIZE / 2;
        let mut contents_s = vec![1; strand_buf_size];
        let mut contents_t = vec![1; strand_buf_size];

        let mut mismatches = 0;
        let mut i = 0;
        let mut offset = 0;

        loop {
            // Refill buffer when compared all the nucleotides in the buffer
            if i == strand_buf_size || i == 0 {
                f.seek(SeekFrom::Start(offset))?;
                f.read(&mut contents_s)?;
                f.seek(SeekFrom::Start(enter_offset_64 + 1 + offset))?;
                f.read(&mut contents_t)?;

                offset += strand_buf_size as u64;

                if i > 0 {
                    i = 0;
                }
            }

            // Break when finding an enter
            if contents_s[i] == b'\n' {
                break;
            }

            // Check for a mismatch between the two sets
            if contents_s[i] != contents_t[i] {
                mismatches += 1;
            }

            i += 1
        }

    println!("Total mismatches: {}", mismatches);

    }
    else {
        println!("Path '{:?}' cannot be found!", loading_path);
    }

    Ok(())
}
