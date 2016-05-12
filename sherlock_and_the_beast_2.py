#!/bin/python

a = [1000000000]
# a = xrange(1, 10000000)

loops = []
negs = []
groups = [0]*4

import time

t1 = time.time()

for n in a:

    # print '---n:', n

    # n=5->33333, n=8->55533333, n=11->55555533333
    # n=16->555 555 33333 33333; 16/5

    # maximize the 5s
    if n % 3 == 0:
        # print n * '5'
        # print 'all fives', n
        # groups[0] += 1
        continue

    # otherwise check for combinations, while maximizing the number of 5s
    max_fives = n / 3  # 5

    loop_counter = 0
    for i in xrange(max_fives, 0, -1):
        # loop_counter += 1
        remainder = n - (i * 3)
        if remainder % 5 == 0:
            print 'groups of 5:', i, 'groups of 3:', remainder / 5
            # print i*'555' + remainder*'3'
            # groups[1] += 1
            break
    else:
        if n % 5 == 0:
            # print n*'3'
            # print 'all threes', n
            # groups[2] += 1
            pass
        else:
            # print '-1'
            # groups[3] += 1
            # negs.append(n)
            pass

    # loops.append(loop_counter)
    # print loop_counter

# if loops:
    # print 'most loops:', max(loops)
# print 'negative ones:', negs
# print 'groups:', groups

# print 'runtime:', time.time() -t1