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
                next_layer[row_num][entry_index + 1].elem += curr_elem # top right
                next_layer[row_num + 1][entry_index].elem += curr_elem # down

        return next_layer

    def __str__(self):
        from os import get_terminal_size
        term_width = get_terminal_size().columns
        result_str = ""
        # Version 1
        # for layer_num in range(len(self.layers)):
        #     result_str += (f"Layer {layer_num}: "
        #                +   str(self.layer_str(self.layers[layer_num])).center(term_width)
        #                +   "\n")
        # return result_str.rstrip("\n")
        # Version 2
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

    def layer_str(self, layer):
        layer_lst = []
        for row in layer:
            result_row = []
            for element in row:
                result_row.append(element.elem)
            layer_lst.append(result_row)

        return layer_lst

    def layer_sum(self, layer_num):
        return 3 ** layer_num

    def nth_dimensional_layer(self, dimension, layer_num):
        return dimension ** layer_num

if __name__ == "__main__":
    test = PascalPyramid(20)
    print(test)
