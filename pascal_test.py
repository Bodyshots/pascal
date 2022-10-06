
def pascal_diagonal_num(diagonal: int, start_pos: int, pos: int) -> int:
    """
    Return the number at <pos> from a <diagonal> sequence
    that begins at <start_pos>.

    Note: <diagonal> should be dependant on the user's input
    <pos> is from the start of the entire sequence (not from <start_pos>)

    >>> pascal_diagonal_num(1, 1, 1)
    1
    >>> pascal_diagonal_num(7, 1, 1)
    1
    >>> pascal_diagonal_num(5, 1, 5)
    70
    >>> pascal_diagonal_num(6, 1, 4)
    56
    >>> pascal_diagonal_num(4, 2, 3)
    10
    >>> pascal_diagonal_num(3, 3, 6)
    21
    >>> pascal_diagonal_num(2, 4, 6)
    6
    >>> pascal_diagonal_num(2, 4, 5)
    5
    >>> pascal_diagonal_num(5, 1, 3) # => (4, 2, 4) => (4, 2, 5)
    15

    """
    if (diagonal == 1 or pos == 1):
        return 1
    if (diagonal == 2):
        return pos
    if (start_pos == 1):
        return pascal_diagonal_num(diagonal - 1, start_pos + 1, pos + 1)
    if (start_pos == 2):
        return pascal_diagonal_num(diagonal, start_pos, pos + 1)

if __name__ == "__main__":
    import doctest
    doctest.testmod()