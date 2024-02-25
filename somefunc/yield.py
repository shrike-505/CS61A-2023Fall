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

class Account:
    """一个余额非零的账户。"""
    interest = 0.02
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
    def deposit(self, amount):
        """存入账户 amount，并返回变化后的余额"""
        self.balance = self.balance + amount
        return self.balance
    def withdraw(self, amount):
        """从账号中取出 amount，并返回变化后的余额"""
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance
    
class CheckingAccount(Account):
    """从账号取钱会扣出手续费的账号"""
    withdraw_charge = 1
    interest = 0.01
    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_charge)
    
class SavingsAccount(Account):
    deposit_charge = 2
    def deposit(self, amount):
        return Account.deposit(self, amount - self.deposit_charge)
    
class AsSeenOnTVAccount(CheckingAccount, SavingsAccount):
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 1 