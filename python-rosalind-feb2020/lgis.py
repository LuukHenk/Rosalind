from pathlib import Path
from typing import Tuple, List

INPUT_PATH = Path("input/rosalind_lgis.txt")
TEST_DATA = (5, 1, 4, 2, 3)
def load_input() -> str:
    with open(INPUT_PATH) as input_file:
        input_data = input_file.readlines()
    return input_data[1]  # pop off the header

def load_permutations(input_data: str) -> Tuple[int]:
    permutations = input_data.split(" ")
    permutations[-1] = permutations[-1][:-1]  # pop off the newline of the last item
    permutations = [int(x) for x in permutations]
    return tuple(permutations)

def create_table(table_size: int) -> List[List[int]]:
    return [table_size*[0] for _ in range(table_size)]

def display_table(table: List[List[int]], columns: Tuple[int]) -> None:
    print("     ", "  ".join([str(column) for column in columns]))
    for i, row in enumerate(table):
        print(i, row)
def main(test=True):
    permutations = TEST_DATA if test else load_permutations(load_input())
    table_size = len(permutations) + 1
    permutations_table = create_table(table_size)
    result = []

    for row_i in range(1, len(permutations_table)):
        for col_i in range(1, len(permutations_table)):
            column_value = permutations[col_i-1]
            if column_value == row_i:
                print(row_i, col_i)
                permutations_table[row_i][col_i] = permutations_table[row_i-1][col_i-1] + 1
                result.append(row_i)
            else:
                previous_col = permutations_table[row_i][col_i-1]
                previous_row = permutations_table[row_i-1][col_i]
                if previous_col > previous_row:
                    permutations_table[row_i][col_i] = previous_col
                else:
                    permutations_table[row_i][col_i] = previous_row
    print(result)
    display_table(permutations_table, columns=permutations)






if __name__ == "__main__":
    # https://www.programiz.com/dsa/longest-common-subsequence
    main()
