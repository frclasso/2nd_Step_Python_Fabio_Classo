#!/usr/bin/env python3

import itertools

# # Infinite counting

# for x in itertools.count(50, 5): # start 50, step 5
#     print(x)
#     if x == 1000:
#         break
# print('Done')

# # Infinite Cycling

# x = 0
# for c in itertools.cycle("RACECAR"):
#     print(c)
#     x += 1
#     if x == 50:
#         break
# print('Done')

# # Infinite repeating
x = 0
for r in itertools.repeat(True):
    print(r)
    x += 1
    if x > 100:
        break
print('Done')