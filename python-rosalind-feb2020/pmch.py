from pathlib import Path

PRACTICE_INP = "AGCUAGUCAU"
INPUT_PATH = Path("input/rosalind_pmch.txt")

def load_input() -> str:
    with open(INPUT_PATH) as input_file:
        input_data = input_file.read()
    input_without_header = "".join(input_data.split("\n")[1:])
    return input_without_header

def factorial_recursive(n):
    return 1 if n == 1 else n * factorial_recursive(n-1)

def main(practice: bool = False):
    sequence = PRACTICE_INP if practice else load_input()
    # Since the sequence contains an equal occurrence of each matching nucleotides, we can just count one of the
    # matching nucleotides
    # To get the amount of matches each matching nucleotide, we can use factorial.
    print(factorial_recursive(sequence.count("A")) * factorial_recursive(sequence.count("C")))


if __name__ == "__main__":
    main()
