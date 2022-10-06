from typing import List

class Queue:
    def __init__(self):
        self._elems = []

    def enqueue(self, elem: "PascalBST"):
        self._elems.append(elem)

    def dequeue(self) -> "PascalBST":
        return self._elems.pop(0)

    def __len__(self) -> int:
        return len(self._elems)

    def peek(self, index) -> "PascalBST":
        """
        Return the <index>th element of the queue.
        """
        return self._elems[index]


class PascalBST:
    def __init__(self, elem=None, left=None, right=None, parent=None):
        if (elem is None):
            self.left = None
            self.right = None
        else:
            self.left = PascalBST(left)
            self.right = PascalBST(right)

        self.root = elem
        self.p = parent
        self.colour = 1 # 1 => White, 0 => Black (visited)


class PascalTriangle:
    def __init__(self, row_num):
        if row_num >= 0:
            self.top = PascalBST(1)
        if row_num >= 1:
            self.top.left = PascalBST(1)
            self.top.right = PascalBST(1)


        for i in range(row_num):
            row_entries = [PascalBST(1, 1)]
            row_entries.extend([PascalBST() for _ in range(j - 1)])
            row_entries.append(PascalBST(1, None, 1))

            prev_row = self.cons_pascal(i - 1)
            for node in row_entries[1: len(row_entries) - 1]:
                new_entry = prev_row[width - 1] + prev_row[width]

        # if row_num == 0:
        #     return PascalBST(1)
        # if row_num == 1:
        #     return PascalBST(1, 1, 1)
        
        # # rows >= 2
        # curr_row = [1]
        # prev_row = self.cons_pascal(row_num - 1)
        # for width in range(1, (row_num + 2) // 2):
        #     curr_row.append(prev_row[width - 1] + prev_row[width])

        # # since pascal's triangle is symmetric, just copy curr_row reversed
        # # note: depending on the triangle's row number, we may have two middle elements
        # # so, we check parity of row_num:
        # # even: no duplicate mid elem
        # # odd: duplicate mid elem
        # if row_num % 2 == 0: # checks parity
        #     curr_row.extend(curr_row[::-1][1:]) # don't dup the mid elem
        # else:
        #     curr_row.extend(curr_row[::-1][:]) # dup the mid elem
        # return curr_row
