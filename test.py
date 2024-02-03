def average(x,y):
    return (x+y)/2

a = 6

def test(x):
    return average(x,a/x)


def div_by_primes(n):
    def iterate(k):
        i = 2
        while i <= n:
            if k % i == 0:
                return True
            i += 1
        return False
    return iterate


def pick(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns True. If there are fewer than K such paragraphs, return
    the empty string.

    Arguments:
        paragraphs: a list of strings
        select: a function that returns True for paragraphs that can be selected
        k: an integer

    >>> ps = ['hi', 'how are you', 'fine']
    >>> s = lambda p: len(p) <= 4
    >>> pick(ps, s, 0)
    'hi'
    >>> pick(ps, s, 1)
    'fine'
    >>> pick(ps, s, 2)
    ''
    """
    # BEGIN PROBLEM 1
    i = -1
    for j in range(k):
        if select(paragraphs[j]) :
            i += 1
            if i == k:
                return paragraphs[j]       
    return ''

    # END PROBLEM 1
ps = ['hi', 'how are you', 'fine']
s = lambda p: len(p) <= 4
pick(ps, s, 0)