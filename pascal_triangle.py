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

    def is_empty(self): return len(self) == 0

    def empty_queue(self):
        for _ in range(len(self._elems)): self.dequeue()


class PascalBST:
    def __init__(self, elem=None, left=None, right=None):
        if (elem is None):
            self.left = None
            self.right = None
        else:
            self.left = PascalBST(left)
            self.right = PascalBST(right)

        self.root = elem
        self.colour = 0 # white => 1, black => 0
    
    def __str__(self): return str(self.root)

class PascalTriangle:
    def __init__(self, row_num):
        if row_num >= 0:
            self.top = PascalBST(1)
            self.vertices = [self.top] # note: technically, self.vertices can basically represent
                                       # pascal's triangle itself, but we'll just ignore that for
                                       # the purposes of making it via BSTs/Graphs 
            if row_num == 0: return
        if row_num >= 1:
            self.top.left = PascalBST(1)
            self.top.right = PascalBST(1)
            self.vertices = [self.top, self.top.left, self.top.right]
            if row_num == 1: return

        self.vertices = [self.top, self.top.left, self.top.right]
        curr_left = self.top.left
        curr_right = self.top.right

        curr_row_queue = Queue()
        next_row_queue = Queue()
        upcoming_row = Queue()
        for i in range(1, row_num):
            # get the nodes for the next lvl
            next_row = self.get_row(i + 1)
            for node in next_row[1: len(next_row) - 1]: 
                next_row_queue.enqueue(node)
                self.vertices.append(node)

            # leftmost col is always 1s
            curr_left.left = PascalBST(1)
            upcoming_row.enqueue(curr_left.left)

            while not (next_row_queue.is_empty() or curr_row_queue.is_empty()):
                next_node = next_row_queue.dequeue()
                upcoming_row.enqueue(next_node)

                curr_left.right, curr_right.left = next_node, next_node

                curr_left = curr_right
                curr_right = curr_row_queue.dequeue()

            # rightmost col is always 1s
            curr_right.right = PascalBST(1)
            if (curr_row_queue.is_empty() and not next_row_queue.is_empty()):
                next_node = next_row_queue.dequeue()
                curr_left.right, curr_right.left = next_node, next_node
            upcoming_row.enqueue(curr_right.right)
        
            curr_row_queue = upcoming_row
            curr_left = curr_row_queue.dequeue()
            curr_right = curr_row_queue.dequeue()
            upcoming_row.empty_queue()

    def __str__(self):
        from os import get_terminal_size
        # basically, BFS traversal, starting from self.top
        for i in self.vertices: i.colour = 0

        nodes_in_lvl = 0
        row_num = 0
        result_str = ""
        queue = Queue()
        self.top.colour = 1
        term_width = get_terminal_size().columns
        queue.enqueue(self.top)
        while not queue.is_empty():
            curr_node = queue.dequeue()

            nodes_in_lvl += 1
            if row_num + 1 == nodes_in_lvl:
                result_str += f"{str(curr_node.root)}\n"
                # prep for next lvl
                nodes_in_lvl = 0
                row_num += 1

            else: result_str += f"{str(curr_node.root)} "
            if curr_node.left and curr_node.left.colour == 0:
                if (curr_node.left.root):
                    curr_node.left.colour = 1
                    queue.enqueue(curr_node.left)
            if curr_node.right.colour == 0:
                if (curr_node.right.root):
                    curr_node.right.colour = 1
                    queue.enqueue(curr_node.right)
            curr_node.colour = 1
        # credit to Zenith for the return statement:
        # https://stackoverflow.com/questions/62549176/python-how-to-center-a-multiline-string-containing-n-for-printing-in-the-ce 
        return "\n".join(line.center(term_width) for line in result_str.split("\n"))

    def get_row(self, row_num):
        if row_num == 0:
            return [PascalBST(1)]
        if row_num == 1:
            return [PascalBST(1), PascalBST(1)]

        # row_num >= 2
        row_entries = [PascalBST(1)]
        row_entries.extend([PascalBST() for _ in range(row_num - 1)])
        row_entries.append(PascalBST(1))
        
        prev_row = self.get_row(row_num - 1)
        for node in range(1, len(row_entries) - 1):
            row_entries[node].root = prev_row[node - 1].root + prev_row[node].root
            row_entries[node].left = PascalBST(None)
            row_entries[node].right = PascalBST(None)

        return row_entries

if __name__ == "__main__":
    test = PascalTriangle(6)
    print(test)
