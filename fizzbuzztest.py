from functools import partial  

multiple_of = lambda base, num: num % base == 0
multiple_3 = partial(multiple_of, 3)
multiple_5 = partial(multiple_of, 5)


def multiple(number):

    if multiple_3(number) and multiple_5(number):
        return 'fizzbuzz'

    elif multiple_3(number):
        return 'fizz'

    elif multiple_5(number):
        return 'buzz'

    else:
        return str(number)


if __name__ == '__main__':
    assert 'fizz' == multiple(3)
    assert 'fizz' == multiple(9)
    assert 'fizz' == multiple(12)

    assert 'buzz' == multiple(5)
    assert 'buzz' == multiple(10)
    assert 'buzz' == multiple(20)

    assert 'fizzbuzz' == multiple(15)
    assert 'fizzbuzz' == multiple(30)
    assert 'fizzbuzz' == multiple(45)
