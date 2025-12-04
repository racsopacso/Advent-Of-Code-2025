import numpy as np
import numpy.typing as npt
from scipy.signal import convolve2d


def get_grid():
    grid = []
    with open("day4_inp.txt", "r") as f:
        for line in f.readlines():
            line = line.strip()
            grid.append([char == "@" for char in line])

    return np.array(grid)


def _sum_grid(grid: npt.NDArray):
    return np.sum(grid, axis=(0, 1))


kernel = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]

grid = get_grid()

old_grid_sum = first_grid_sum = _sum_grid(grid)

while True:
    conv = convolve2d(grid, np.array(kernel), mode="same") > 3

    grid = grid * conv

    grid_sum = _sum_grid(grid)

    if grid_sum == old_grid_sum:
        break

    old_grid_sum = grid_sum

print(first_grid_sum - grid_sum)
