# #!/bin/python

# import sys


# t = int(raw_input().strip())
# for a0 in xrange(t):
#     n = int(raw_input().strip())

#     print '---n:', n,

#     if (n-5) % 3 != 0 and (n-3) % 5 != 0:
#         print -1
#         continue

#     # n=5->33333, n=8->55533333, n=11->55555533333
#     elif (n-5) % 3 == 0:

#         num_fives = n / 3
#         # maximize the number of 5 groups
#         for i in xrange(num_fives, 0, -1):
#             if (n - i*3) % 5 == 0:
#                 num_fives = i
#                 break
#             else:
#                 num_fives = 0
#         num_threes = (n - num_fives*3) / 5
#         print num_fives*'555' + num_threes*'33333'

#     # n=3->555, n=6->555555
#     elif (n-3) % 5 == 0:

#         num_fives = n / 3
#         # maximize the number of 5 groups
#         for i in xrange(num_fives, 0, -1):
#             if (n - i*3) % 5 == 0:
#                 num_fives = i
#                 break
#             else:
#                 num_fives = 0
#         num_threes = (n - num_fives*3) / 5
#         print num_fives*'555' + num_threes*'33333'


a = [1000000000]
# a = xrange(1, 10000000)

import time

t1 = time.time()

for n in a:

    # print '---n:', n,

    if n % 3 == 0:
        # print '5'*n
        pass

    elif n >= 8:
        sets_of_three = 0
        if (n-5) % 3 == 2:
            sets_of_three = 2
        else:
            sets_of_three = 1
        sets_of_five = n - (5 * sets_of_three)

        print 'groups of 5:', sets_of_five/3, 'groups of 3:', sets_of_three
        # print '5'*sets_of_five + '33333'*sets_of_three

# print 'runtime:', time.time() -t1