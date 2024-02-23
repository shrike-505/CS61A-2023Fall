# def prefixes(string):
#     if string:
#         yield from prefixes(string[:-1])
#         yield string


# def countdown(index):
#     if index>0:
#         print (index)
#         yield index
#         yield from countdown(index-1)

def partitions(n, m):
    """Return a generator of all partitions of n using parts of up to m.

    Args:
        n (int): The number to partition.
        m (int): The largest part to use in the partition.
    >>> for k in partitions(6, 4):  print(k)
    2+4
    1+1+4
    3+3
    1+2+3
    1+1+1+3
    2+2+2
    1+1+2+2
    1+1+1+1+2
    1+1+1+1+1+1
    """
    if n > 0 and m > 0:
        if n == m:
            yield str(m)
        for p in partitions(n-m, m):
            yield str(p) + '+' + str(m)


        yield from partitions(n, m-1)

def differences(it):
    """ 
    Yields the differences between successive terms of iterable it.

    >>> d = differences(iter([5, 2, -100, 103]))
    >>> [next(d) for _ in range(3)]
    [-3, -102, 203]
    >>> list(differences([1]))
    []
    """
    prev = next(it)
    for curr in it:
        yield curr - prev
        prev = curr

def generate_constant(x):
    """A generator function that repeats the same value X forever.
    >>> two = generate_constant(2)
    >>> next(two)
    2
    >>> next(two)
    2
    >>> sum([next(two) for _ in range(100)])
    200
    """
    while True:
        yield x

def black_hole(seq, trap):
    """A generator that yields items in SEQ until one of them matches TRAP, in
    which case that value should be repeatedly yielded forever.
    >>> trapped = black_hole([1, 2, 3], 2)
    >>> [next(trapped) for _ in range(6)]
    [1, 2, 2, 2, 2, 2]
    >>> list(black_hole(range(5), 7))
    [0, 1, 2, 3, 4]
    """
    for elem in seq:
        if elem == trap:
            yield from generate_constant(trap)
        else:
            yield elem