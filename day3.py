from itertools import chain
import re
import typing as t

from itertools import pairwise


def _yield_rows():
    with open("day3_inp.txt", "r") as f:
        for line in f.readlines():
            # regex for old times' sake
            ret = re.findall(r"\d", line)

            yield [int(elem) for elem in ret]


def _get_val(introw: t.Sequence[int]):
    tot = 0
    for idx, val in enumerate(reversed(introw)):
        tot += val * (10**idx)

    return tot


def get_largest_val(introw: t.Sequence[int], idx: int = 12):
    current_arr, remaining_arr = introw[:idx], introw[idx:]

    for num in remaining_arr:
        for idx, (first_num, second_num) in enumerate(
            pairwise(chain(current_arr, [num]))
        ):
            if second_num >= first_num:
                proposed = list(chain(current_arr[:idx], current_arr[idx + 1 :], [num]))

                if _get_val(proposed) > _get_val(current_arr):
                    current_arr = proposed

                    break

    return _get_val(current_arr)


print(sum(get_largest_val(introw) for introw in _yield_rows()))
