from functools import cache
from itertools import chain, product, combinations, repeat
import math
import re

# yeah I'm using something that's not stdlib
# deal with it
# looking at this code pretty clear it isn't shortcutting past anything interesting
from sympy.ntheory import factorint


def _yield_ranges():
    with open("day2_inp.txt", "r") as f:
        line = f.read()

    # regex for dazza
    ret = re.findall(r"(\d+)-(\d+)", line)

    for start, end in ret:
        yield (int(start), int(end))


def _yield_non_equal_factors_of(power: int):
    """
    Yields every factor of the power that is not the number itself

    This is because we disallow a single repetition to count as a repetition.
    """
    factors: dict[int, int] = factorint(power)

    factor_list = list(
        chain.from_iterable(repeat(num, exp) for num, exp in factors.items())
    )

    for comb_len in range(len(factor_list)):
        for comb_tup in combinations(factor_list, comb_len):
            yield math.prod(comb_tup)


def _yield_legal_multiples_for_power(power: int):
    """
    Yields numbers that are factors of every number with the repeated digit property we want to see
    within a given order of magnitude

    For example: for order of magnitude 2, every repeated number is just a multiple of 11
    For order of magnitude 4, they're all multiples of 1010 or 1111 or 0101 aka 101
    """
    for factor in _yield_non_equal_factors_of(power):
        comb_multiply_factor = power // factor

        for comb in product(["1", "0"], repeat=factor):
            srepr = (("".join(comb)) * comb_multiply_factor).lstrip("0")

            if srepr == "":
                continue

            yield int(srepr)


@cache
def _get_legal_multiples_for_power(power: int):

    # using frozenset because we can get duplicates
    # for example: consider an 8-long number
    # we could have 4 lots of 10 or 2 lots of 1010
    # both giving 10101010 as a legal multiple
    return frozenset(_yield_legal_multiples_for_power(power))


def _get_bad_nums_at_power(start: int, end: int, power: int):
    legal_multiples = _get_legal_multiples_for_power(power)

    start = max(start, int("1" + "0" * (power - 1)))
    end = min(end, int("9" * power))

    for multiple in legal_multiples:
        val = max(math.ceil(start / multiple) * multiple, multiple)

        while val <= end:
            yield val
            val += multiple


def _get_power(num: int):
    return math.floor(math.log(num, 10))


def _get_bad_nums_power_independent(start: int, end: int):
    start_power = max(_get_power(start), 2)
    end_power = _get_power(end) + 2

    for power in range(start_power, end_power):
        yield from _get_bad_nums_at_power(start, end, power)


print(
    sum(
        set(
            chain.from_iterable(
                _get_bad_nums_power_independent(*tup) for tup in _yield_ranges()
            )
        )
    )
)
