from typing import List

def get_next_layer(prev_layer: List[int]):

    next_layer = []
    for i in range(len(prev_layer[0]) + 1, 0, -1):
        next_layer.append([1 for j in range(i)])
    return next_layer

if __name__ == "__main__":
    print(get_next_layer([[1, 1], [1]]))
