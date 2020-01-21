import numpy as np
row1 = "1234567890"  # `=
row2 = "qwertyuiop"  # []\
row3 = "asdfghjkl"   # ;'
row4 = "zxcvbnm"     # ,./
srow1 = "~!@#$%^&*()_+"
srow2 = "{}|"
srow3 = ":\""
srow4 = "<>?"

all_chars = row1 + row2 + row3 + row4

            # + srow1 + srow2 + srow3 + srow4

dists = []
log = []
fib = [0, 1, 2]
for i in range(1, 14):
    log.append(np.log(i)*i)
for i in range(10):
    next = fib[-1] + fib[-2]
    if next >= 55:
        next = 55
    fib.append(next)
print(fib)
norm_log = list(np.array(log) / max(log))
print(norm_log)
print(log)
for i in range(1, len(log)):
    print(log[i]-log[i-1])
#   q w e r t y  u  i  o  p  a s d f g  h  j  k  l  z x c v  b  n  m
# q 0 1 3 4 7 11 18 29 47 76 1 3 4 7 11 18 29 47 76 3 4 7 11 18 29 47
# w 1 0 1 3 4 7  11 18 29 47 3 1 3 4 7  11 18 29 47 4 3 4 7  11 18 29
# e 3 1 0 1 3 4  7  11 18 29 4 3 1 3 4  7  11 18 29 7 4 3 4  7  11 18
# r 4 3 1 0 1
# t 7 4 3 1 0
# y
# u
# i
# o
# p

# dist = []
rows = [row1, row2, row3, row4]
# for row in rows:
#     row_i = rows.index(row)
#     for i in range(len(row)):
#         dist.append(fib[i+row_i])
# print(dist, len(dist))

# dist = []
# offset = 20
# for row in rows:
#     row_i = rows.index(row)
#     over = list(range(1, min(len(row)+1, offset + 1)))[::-1] + list(range(len(row)-offset))
#     print(over)
#     for i in over:
#         dist.append(fib[i + row_i])
# print(len(dist), dist)


def make_over(char, all_chars, rows) -> list:
    over = []
    for row in rows:
        if char in row:
            row_index = row.index(char)
            rows_index = rows.index(row)
            break

    for row in rows:
        part_over = [-1 for i in range(len(row))]
        offset = abs(rows_index - rows.index(row))
        if len(row) <= row_index:
            part_over[-1] = abs(len(row)-row_index) + 1 + offset
        else:
            part_over[row_index] = offset
        over += part_over

    row_start = 0
    row_end = 0
    prev_len = 0
    for row in rows:
        row_start += prev_len
        prev_len = len(row)
        row_end += len(row)
        match_index = [index for index in range(row_start, row_end) if over[index] != -1][0]

        match = over[match_index]
        left = len(row) - row_index
        if left < 1:
            left = 1
        for i in range(1, left):
            over[match_index+i] = i + match
        right = len(row) - left + 1
        for i in range(1, right):
            over[match_index-i] = i + match
    # print(over)
    return over


# make_over('9', all_chars, rows)

header = ' '
for char in all_chars + ' ':
    header += f'{char:>5}'
print(header)
print()

dists = []
for char in all_chars:
    dist = []
    for over in make_over(char, all_chars, rows):
        dist.append(log[over])
    dists.append(dist)
    line = f'{char}'
    for d in dist:
        line += f'{d:5.1f}'
    print(line)

dists = np.array(dists)
dists = dists / dists.max()
print(dists)

np.save('qwert.npy', dists)
np.save('chars.npy', all_chars)
dists.max()





