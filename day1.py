
import re
import typing as t

def _parse_lines():
    with open("day1_inp.txt") as f:
        for line in f.readlines():
            left = re.match(r"L(\d+)", line)
            
            if left is not None:
                yield -int(left.group(1))
                continue

            right = re.match(r"R(\d+)", line)

            if right is not None:
                yield int(right.group(1))

def _yield_zero_points_better(line_iter: t.Iterable[int]):
    val = 50

    for num in line_iter:
        if num == 0:
            continue

        parity = 1 if num > 0 else -1
        
        guaranteed_clicks = abs(num) // 100
        remainder = (abs(num) % 100) * parity

        yield guaranteed_clicks

        new_val = val + remainder
        new_val_mod = new_val % 100

        if ((new_val_mod != new_val) or (new_val_mod == 0)) and (val != 0):
            yield 1

        val = new_val_mod

print(sum(_yield_zero_points_better(_parse_lines())))