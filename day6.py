from itertools import zip_longest
import math
import re

def process_ret(ret: list[tuple[str, ...]]):
    num_tups: list[list[str]] = []
    ops: set[str] = set()
    
    for tup in ret:
        *nums, op = tup

        num_tups.append(nums)
        if op in ("*", "+"):
            ops.add(op)
    
    if len(ops) == 1:
        final_op = next(iter(ops))
        yield final_op, num_tups

def get_question():
    with open("day6_inp.txt", "r") as f:
        rows = [list(line.strip("\n")) for line in f.readlines()] 
    
    tposed = tuple(zip_longest(*rows, fillvalue=" "))

    line_len = len(tposed[0])

    split_tup = (" ",) * line_len

    ret: list[tuple[str, ...]] = []

    for tup in tposed:
        if tup == split_tup:
            yield from process_ret(ret)
            
            ret = []
        
        else:
            ret.append(tup)
    
    yield from process_ret(ret)
    
def process_question():
    for operation, num_tups in get_question():
        nums = [int("".join(num_tup).strip()) for num_tup in num_tups]

        match operation:
            case "+":
                yield sum(nums)
            case "*":
                yield math.prod(nums)

print(sum(process_question()))