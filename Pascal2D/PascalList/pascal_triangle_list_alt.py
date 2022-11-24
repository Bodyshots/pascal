from typing import List

class PascalTriangle:
    def __init__(self, height):
        self.height = height
        self.rows = [self.get_row(i) for i in range(height)]

    def __str__(self):
        # Meru Prastaara ver (left-aligned)
        # result_str = "["
        # for i in self.rows: result_str += str(i) + "\n"
        # return result_str.rstrip("\n") + "]"

        # Pascal Triangle ver
        from os import get_terminal_size
        term_width = get_terminal_size().columns
        result_str = ""
        for i in self.rows: result_str += str(i).center(term_width) + "\n"
        return result_str.rstrip("\n")

    def get_row(self, row_num):
        if row_num < 0 or row_num > self.height:
            return -1
        if row_num == 0:
            return [1]
        if row_num == 1:
            return [1, 1] # will always be [1, x, 1], where x is a certain # of elems
        
        # rows >= 2
        return self.get_next_row(self.get_row(row_num - 1))

    def get_next_row(self, prev_row: List[int]):
        next_row_num = len(prev_row)
        curr_row = [1]

        # pascal's recursive definition
        for width in range(1, (next_row_num + 2) // 2):
            curr_row.append(prev_row[width - 1] + prev_row[width])

        # since pascal's triangle is symmetric, just copy curr_row reversed
        # note: depending on the triangle's row number, we may have two middle elements
        # so, we check parity of row_num:
        # even: no duplicate mid elem
        # odd: duplicate mid elem
        if next_row_num % 2 == 0: # checks parity
            curr_row.extend(curr_row[::-1][1:]) # don't dup the mid elem
        else: curr_row.extend(curr_row[::-1][:]) # dup the mid elem
        return curr_row

    def pascal_sum(self, row_num): # complexity: O(1) ez
        return 2 ** row_num

    def get_entry(self, row_num, col_num):
        if ((row_num < 0 or row_num > self.height) or 
            (len(self.rows[row_num]) < col_num or col_num < 0)):
            return -1
        return self.rows[row_num][col_num]
