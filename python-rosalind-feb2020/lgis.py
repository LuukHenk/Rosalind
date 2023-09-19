from pathlib import Path
from typing import List

INPUT_PATH = Path("input/rosalind_lgis.txt")
TEST_DATA = [5, 1, 4, 2, 3]
PermutationTable = List[List[int]]

def load_input() -> str:
    with open(INPUT_PATH) as input_file:
        input_data = input_file.readlines()
    return input_data[1]  # pop off the header

def load_permutations(input_data: str) -> List[int]:
    permutations = input_data.split(" ")
    permutations[-1] = permutations[-1][:-1]  # pop off the newline of the last item
    permutations = [int(x) for x in permutations]
    return permutations

def create_table(table_size: int) -> PermutationTable:
    return [table_size*[0] for _ in range(table_size)]

def display_table(table: PermutationTable, columns: List[int]) -> None:
    print("     ", "  ".join([str(column) for column in columns]))
    for i, row in enumerate(table):
        print(i, row)

def create_permutations_table(permutations: List[int]) -> PermutationTable:
    table_size = len(permutations) + 1
    permutations_table = create_table(table_size)
    for row_i in range(1, len(permutations_table)):
        for col_i in range(1, len(permutations_table)):
            column_value = permutations[col_i-1]
            if column_value == row_i:
                permutations_table[row_i][col_i] = permutations_table[row_i-1][col_i-1] + 1
            else:
                previous_col = permutations_table[row_i][col_i-1]
                previous_row = permutations_table[row_i-1][col_i]
                if previous_col > previous_row:
                    permutations_table[row_i][col_i] = previous_col
                else:
                    permutations_table[row_i][col_i] = previous_row
    return permutations_table

def find_fastest_route_in_permutation_table(permutation_table: PermutationTable, permutations: List[int]) -> List[int]:
    value_path = []
    current_col = len(permutation_table) - 1
    current_row = len(permutation_table) - 1
    current_value = permutation_table[current_row][current_col]
    while current_row != 0 and current_col != 0:
        if permutation_table[current_row-1][current_col] == current_value:
            current_row -= 1
        elif permutation_table[current_row][current_col-1] == current_value:
            current_col -= 1
        else:
            value_path.append(permutations[current_col-1])
            current_row -= 1
            current_col -= 1
            current_value = permutation_table[current_row][current_col]
    value_path.reverse()
    return value_path

def main(test=False):
    permutations = TEST_DATA if test else load_permutations(load_input())
    permutations_table = create_permutations_table(permutations)
    # display_table(permutations_table, columns=permutations)
    value_path = find_fastest_route_in_permutation_table(permutations_table, permutations)
    print(" ".join([str(x) for x in value_path]))


    permutations.reverse()
    permutations_table = create_permutations_table(permutations)
    # display_table(permutations_table, columns=permutations)
    value_path = find_fastest_route_in_permutation_table(permutations_table, permutations)
    value_path.reverse()
    print(" ".join([str(x) for x in value_path]))








if __name__ == "__main__":
    # https://www.programiz.com/dsa/longest-common-subsequence
    main()
