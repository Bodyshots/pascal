from turtle import right
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
        return
        if (layers == 0):
            self.layers = [[[1]]]
            return Pascal3DElem(1)

        self.layers = [[1]]
        for _ in range(layers + 1):
            self.layers.append(self.get_next_layer(self.layers))
        
    
    def get_next_layer(self, prev_layer: List[List[Pascal3DElem]]):
        """
        Structure of a layer will be a list with lists of decreasing length

        Eg.
        
        Layer 0: [[1]]

        Layer 1: [[1, 1], [1]]

        Layer 2:[[1, 2, 1], [2, 2], [1]]

        Layer 3: [[1, 3, 3, 1], [3, 6, 3], [3, 3], [1]]

        """

        next_layer = []
        for i in range(len(prev_layer[0]) + 1, 0, -1):
            next_layer.append([Pascal3DElem() for _ in range(i)])
        
        for row_num in range(len(prev_layer)):

            for entry_index in range(len(prev_layer[row_num])):

                curr_elem = prev_layer[row_num][entry_index].elem
                next_layer[row_num][entry_index].elem += curr_elem # top left
                next_layer[row_num][entry_index + 1].elem += curr_elem
                next_layer[row_num + 1][entry_index].elem += curr_elem

        return next_layer

if __name__ == "__main__":
    test = PascalPyramid(1)
    test_layer1 = test.get_next_layer([[Pascal3DElem(1)]])
    test_layer2 = test.get_next_layer([[Pascal3DElem(1), Pascal3DElem(1)], [Pascal3DElem(1)]])

    def get_output(output_layer):
        output = []
        for row in output_layer:
            result_row = []
            for element in row:
                result_row.append(element.elem)
            output.append(result_row)

        return output

    print(get_output(test.get_next_layer(test_layer2)))
