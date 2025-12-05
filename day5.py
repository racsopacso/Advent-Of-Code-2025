import re

def get_data():
    with open("day5_inp.txt", "r") as f:
        out = f.read()
    
    fresh_ranges, _ = out.split("\n\n")

    ranges_found = re.findall(r"(\d+)-(\d+)", fresh_ranges)

    tup_gen = ((int(el1), int(el2)) for el1, el2 in ranges_found)

    return sorted(tup_gen, key=lambda x: x[0])

def get_ranges():
    tup, *remaining = get_data()

    for start, end in remaining:
        if start <= tup[1]:
            tup = (tup[0], max(end, tup[1]))
        
        else:
            yield tup
            tup = (start, end)
    
    yield tup

total = 0
for start, end in get_ranges():
    total += (end - start + 1)

print(total)