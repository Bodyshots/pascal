from typing import List

class Pascal3DElem:
    def __init__(self, elem=0):
        self.elem = elem

    def __str__(self):
        return str(self.elem)

class PascalPyramid:
    """
    A PascalPyramid will be a list of list of list of Pascal3DElems.
    In other words, a PascalPyramid will be represented by a list with
    2 nested lists with a series of Pascal3DElems at the lowest depth.
    
    """
    def __init__(self, layers):
        if (layers == 0):
            self.layers = [[[Pascal3DElem(1)]]]
        else:
            self.layers = [[[Pascal3DElem(1)]]]
            for i in range(layers):
                self.layers.append(self.get_next_layer(self.layers[i]))
    
    def get_next_layer(self, prev_layer: List[List[Pascal3DElem]]):
        """
        The structure of a layer will be a list with lists of 
        decreasing length

        Eg.
        Layer 0: [[1]]
        Layer 1: [[1, 1], [1]]
        Layer 2:[[1, 2, 1], [2, 2], [1]]
        Layer 3: [[1, 3, 3, 1], [3, 6, 3], [3, 3], [1]]

        Neat observations:
        1. The bottom row (ie. the base of a layer, or the row w/ the most
         amount of entries) of an nth layer has a sum of 2 ** n
        2. The corners of a layer are always 1
            a) The adjacent entries to these corners always correspond to
            the current layer number
        3. Every third layer only has one number that is the greatest
        among all entries
            a) This entry will always be surrounded by six identical 
                entries that are the second-most greatest among all entries
            b) Otherwise, the layer will have three identical entries that are the
            greatest among all entries
        4. The sum of the nth layer is 3 ** n
        5. Every layer is symmetric in three ways (from each side of a layer)
        6. All sides of a layer correspond to the mth row of Pascal's Triangle
        7. The number of elements in the nth layer is nth element in the sequence
        of triangular numbers (ie. 1, 3, 6, 10, 15,...)
            a) "Triangular" numbers as in the number of items (eg. balls) needed
            to make a triangle
            b) This can also be interpreted as being the greatest number in
            Pascal Triangle's third column
            c) Formula of this sequence is ((n + 1)(n + 2)/2) (via Wikipedia),
            which is similar to the closed-form expression to sum the
            sequence 1 + 2 + 3 + 4 +...+ n.
        8. Each entry in the nth layer corresponds to a number in a trinomial
        raised to the n after being expanded.
        9. Considering how a 2D and 3D Pascal shape is modelled using lists, 
        one could assume that a "4D Pascal Shape" would consist of 4 nested lists,
        with the second-nested list being the structure for a 3D Pascal Pyramid.
            a) From this, one could assume that making a Pascal shape in n
            dimensions would take at least n nested lists (to be proven).
             

        """

        next_layer = []
        for i in range(len(prev_layer[0]) + 1, 0, -1):
            next_layer.append([Pascal3DElem() for _ in range(i)])

        for row_num in range(len(prev_layer)):
            for entry_index in range(len(prev_layer[row_num])):
                curr_elem = prev_layer[row_num][entry_index].elem
                next_layer[row_num][entry_index].elem += curr_elem # top left
                next_layer[row_num][entry_index + 1].elem += curr_elem # top right
                next_layer[row_num + 1][entry_index].elem += curr_elem # down

        return next_layer

    def __str__(self):
        from os import get_terminal_size
        term_width = get_terminal_size().columns
        result_str = ""
        for layer in self.layers:
            curr_layer = self.layer_str(layer)[::-1]
            for row_num, row in enumerate(curr_layer): 
                for element in row:
                    result_str += f"{str(element)} "
                result_str += "\n"
                # result_str += str(row) + "\n" => for [] on each row
                if (row_num == len(curr_layer) - 1): 
                    result_str += f"Layer {row_num}\n\n"
        return "\n".join(line.center(term_width) for line in result_str.split("\n"))

    def layer_str(self, layer: List[List[Pascal3DElem]]):
        layer_lst = []
        for row in layer:
            result_row = []
            for element in row:
                result_row.append(element.elem)
            layer_lst.append(result_row)

        return layer_lst

    def layer_sum(self, layer_num: int):
        """
        As a result of observation 4 in the get_next_layer function
        """
        return 3 ** layer_num

    def nth_dimensional_layer(self, dimension: int, iteration: int):
        """
        Taking into account that the sum of Pascal's Triangle is
        2 ** n, where n is the height of the triangle, and the sum
        of Pascal's Pyramid (observation 4), we could predict the
        sum of any "Pascellian" structure to be dimension ** iteration.

        The proof of this fact is left as an exercise to the reader.
        """
        return dimension ** iteration

    def find_pyramid_max(self):
        return self.find_max(self.layers[len(self.layers) - 1])

    def find_max(self, layer: List[List[Pascal3DElem]]):
        layer_num = len(layer) - 1
        first_index = layer_num - (int(round(layer_num / 3)))
        second_index = (int(round(layer_num / 3)))
        return layer[first_index][second_index].elem
