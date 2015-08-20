__author__ = 'cloud'


def fabnaci(n):
    return n if n == 1 else n * fabnaci(n - 1)


# max recursion depth exceeded
# print fabnaci(1000)


def fabnaci_with_tail_recursion(n, total=1):
    if n == 1:
        return total
    total *= n
    return fabnaci_with_tail_recursion(n - 1, total)


# python don't support tail recursion
# print fabnaci_with_tail_recursion(1000)


# use loop instead
def fabnaci_with_loop(n):
    ret = 1
    count = 0
    while n > 1:
        ret = ret * n
        n -= 1
        count += 1
    else:
        return count + 1, ret


print fabnaci_with_loop(100)
