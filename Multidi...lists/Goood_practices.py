matrix = [
    [1, 2, 3, 4],
    [2, 3, 4, 5],
    [3, 4, 5, 6],

]
# BAD
print([[x for x in row if x % 2 == 0] for row in matrix])


# Correct // mnogo po razbiraemo li e

def is_even(number):
    return number % 2 == 0


def get_even(ll):
    return [x for x in ll if is_even(x)]


print([get_even(row) for row in matrix])
