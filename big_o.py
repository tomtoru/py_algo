
def func_1(ns):
    """
    O(1)
    """
    return ns[0]

def func_2(n):
    """
    O(log(n))
    """
    if n <= 1:
        return
    else:
        print(n)
        func_2(n/2)

def func_3(ns):
    """
    O(n)
    """
    for n in ns:
        print(n)

def func_4(n):
    """
    O(n * log(n))
    """
    for i in range(int(n)):
        print(i, end=' ')
    print()

    if n <= 1:
        return

    func_4(n/2)

def func_5(ns):
    """
    O(n**2)
    """
    for i in range(len(ns)):
        for j in range(len(ns)):
            print(ns[i], ns[j])
        print()

if __name__ == "__main__":
    func_4(10)
    func_5([1,2,3,4,5])
