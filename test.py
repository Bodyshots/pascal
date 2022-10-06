def cons_pascal(row_num):
    if row_num == 0:
        return [1]
    if row_num == 1:
        return [1, 1] # will always be [1, x, 1], where x is a certain # of elems
    
    # rows >= 2
    curr_row = [1]
    prev_row = cons_pascal(row_num - 1)
    for width in range(1, (row_num + 2) // 2):
        curr_row.append(prev_row[width - 1] + prev_row[width])

    # since pascal's triangle is symmetric, just copy curr_row reversed
    # note: depending on the triangle's row number, we may have two middle elements
    # so, we check parity of row_num:
    # even: no duplicate mid elem
    # odd: duplicate mid elem
    if row_num % 2 == 0: # checks parity
        curr_row.extend(curr_row[::-1][1:]) # don't dup the mid elem
    else:
        curr_row.extend(curr_row[::-1][:]) # dup the mid elem
    return curr_row

def pascal_sum(row_num):
    return sum(cons_pascal(row_num))

    
    #recursive case
    # will need to append <rows> times
    """
    Eg visualizaton:
    0    [[1],
    1    [1, 1],
    2    [1, 2, 1],
    3    [1, 3, 3, 1],
    4    [1, 4, 6, 4, 1],
    5    [1, 5, 10, 10, 5, 1],
    6    [1, 6, 15, 20, 15, 6, 1]]
    """

if __name__ == "__main__":
    print(cons_pascal(10))
    print(pascal_sum(10))
