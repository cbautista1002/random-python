# Writing programming interview questions hasn't made me rich. Maybe trading Apple stocks will. Suppose we could access yesterday's stock prices as a list, where:

# The indices are the time in minutes past trade opening time, which was 9:30am local time.
# The values are the price in dollars of Apple stock at that time.

# So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.

# Write an efficient function that takes stock_prices_yesterday and returns the best profit I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.

# For example:

#   stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

# get_max_profit(stock_prices_yesterday)
# # returns 6 (buying for $5 and selling for $11)

# No "shorting" - you must buy before you sell. You may not buy and sell in the same time step (at least 1 minute must pass).

def get_max_profit(stock_prices_yesterday):

    max_profit = 0

    # go through every time
    for outer_time in xrange(len(stock_prices_yesterday)):

        # for every time, go through every OTHER time
        for inner_time in xrange(len(stock_prices_yesterday)):

            # for each pair, find the earlier and later times
            earlier_time = min(outer_time, inner_time)
            later_time   = max(outer_time, inner_time)

            # and use those to find the earlier and later prices
            earlier_price = stock_prices_yesterday[earlier_time]
            later_price   = stock_prices_yesterday[later_time]

            # see what our profit would be if we bought at the
            # earlier price and sold at the later price
            potential_profit = later_price - earlier_price

            # update max_profit if we can do better
            max_profit = max(max_profit, potential_profit)

    return max_profit


def get_max_profit2(stock_prices_yesterday):

    max_profit = 0

    # go through every price (with its index as the time)
    for earlier_time, earlier_price in enumerate(stock_prices_yesterday):

        # and go through all the LATER prices
        for later_price in stock_prices_yesterday[earlier_time+1:]:

            # see what our profit would be if we bought at the
            # earlier price and sold at the later price
            potential_profit = later_price - earlier_price

            # update max_profit if we can do better
            max_profit = max(max_profit, potential_profit)

    return max_profit


def get_max_profit3(stock_prices_yesterday):

    min_seen = stock_prices_yesterday[0]
    max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]

    for index, price in enumerate(stock_prices_yesterday):

        if index == 0:
            continue

        current_diff = price - min_seen

        if current_diff > max_profit:
            print 'found new max of %s at %s' % (current_diff, index)
            print 'price = %s, min_seen = %s' % (price, min_seen)
            max_profit = current_diff

        if price < min_seen:
            min_seen = price
            print 'new min %s at %s' % (min_seen, index)

    return max_profit



# print get_max_profit([33,15,37,29,24,2]) # 22
# print get_max_profit2([33,15,37,29,24,44,2,26,45])
# print get_max_profit3([33,15,37,29,24,44,2,26,45])
# print get_max_profit2([45, 33, 24, 22, 10, 9, 2])
# print get_max_profit3([45, 33, 24, 22, 10, 9, 2])








#################################################################
#################################################################
# https://www.interviewcake.com/question/python/product-of-other-numbers
#################################################################
#################################################################

# You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.
# Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.
# For example, given:
#   [1, 7, 3, 4]
# your function would return:
#   [84, 12, 28, 21]
# by calculating:
#   [7*3*4, 1*3*4, 1*7*4, 1*7*3]
# Do not use division in your solution.


def get_products_of_all_ints_except_at_index(input_list):

    new_list = []

    # for index, value in enumerate(input_list):
    #     temp = input_list[:]
    #     temp.pop(index)
    #     new_list.append

    for index, value in enumerate(input_list):
        new_list.append(
            reduce(lambda x, y: x*y, input_list[0:index]+input_list[index+1:])
        )

    return new_list

# assert get_products_of_all_ints_except_at_index([1, 7, 3, 4])    == [84, 12, 28, 21]
# assert get_products_of_all_ints_except_at_index([1, 7, 3, 4, 0]) == [0, 0, 0, 0, 84]








#################################################################
#################################################################
# https://www.interviewcake.com/question/python/highest-product-of-3
#################################################################
#################################################################

# Given a list_of_ints, find the highest_product you can get from three of the integers.
# The input list_of_ints will always have at least three integers.

a = [1, 7, 3, 4, 1, 5, 2, -9, -2, -3, -4, -1, 2, 5, 6] # 1, 1, 3, 4, 7
b = [7, -2, 1, 9, 1, 4, 7, -3, -7, -8, -1, -2, 5, 7, 9] # -2, 1, 7, 9
c = [7, -2, 1, -9, 3, 6, 9, 0, -1, -5, -3, -6, -8, 0, 1] # -9, -2, 1, 7
# if there are two negative numbers then perhaps they should be included

def max_prod(input_ints):
    a = sorted(input_ints)
    cur_highest = 0

    max_index_to_check = len(a) - 3

    for i, e in enumerate(a):
        print '\ni:', i, 'e:', e
        # Check for 3 in a row
        in_a_row = reduce(lambda x,y:x*y, a[i:i+3])
        print 'in_a_row', in_a_row
        cur_highest = max(cur_highest, in_a_row)
        if i > max_index_to_check:
            continue
        # Check for cur + last two
        cur_last_two = reduce(lambda x,y:x*y, [a[i]]+a[-2:])
        print 'cur_last_two', cur_last_two
        cur_highest = max(cur_highest, cur_last_two)
        # Check for cur+next+last
        cur_next_last = reduce(lambda x,y:x*y, a[i:i+2]+[a[-1]])
        print 'cur_next_last', cur_next_last
        cur_highest = max(cur_highest, cur_next_last)

    print '############### cur_highest:', cur_highest
    return cur_highest

# max_prod(a)
# max_prod(b)
# max_prod(c)

def highest_product_of_3(list_of_ints):
    if len(list_of_ints) < 3:
        raise Exception('Less than 3 items!')

    # We're going to start at the 3rd item (at index 2)
    # so pre-populate highests and lowests based on the first 2 items.
    # we could also start these as None and check below if they're set
    # but this is arguably cleaner
    highest = max(list_of_ints[0], list_of_ints[1])
    lowest =  min(list_of_ints[0], list_of_ints[1])

    highest_product_of_2 = list_of_ints[0] * list_of_ints[1]
    lowest_product_of_2  = list_of_ints[0] * list_of_ints[1]

    # except this one--we pre-populate it for the first /3/ items.
    # this means in our first pass it'll check against itself, which is fine.
    highest_product_of_three = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]

    # walk through items, starting at index 2
    for current in list_of_ints[2:]:

        # do we have a new highest product of 3?
        # it's either the current highest,
        # or the current times the highest product of two
        # or the current times the lowest product of two
        highest_product_of_three = max(
            highest_product_of_three,
            current * highest_product_of_2,
            current * lowest_product_of_2)

        # do we have a new highest product of two?
        highest_product_of_2 = max(
            highest_product_of_2,
            current * highest,
            current * lowest)

        # do we have a new lowest product of two?
        lowest_product_of_2 = min(
            lowest_product_of_2,
            current * highest,
            current * lowest)

        # do we have a new highest?
        highest = max(highest, current)

        # do we have a new lowest?
        lowest = min(lowest, current)

    return highest_product_of_three


# assert max_prod(a) == highest_product_of_3(a)
# assert max_prod(b) == highest_product_of_3(b)
# assert max_prod(c) == highest_product_of_3(c)











#################################################################
#################################################################
# https://www.interviewcake.com/question/python/merging-ranges
#################################################################
#################################################################

# Your company built an in-house calendar tool called HiCal. You want to add a
# feature to see the times in a day when everyone is available.
# To do this, you'll need to know when any team is having a meeting. In HiCal, a
# meeting is stored as tuples of integers (start_time, end_time). These integers
# represent the number of 30-minute blocks past 9:00am.

# For example:

# (2, 3) # meeting from 10:00 - 10:30 am
# (6, 9) # meeting from 12:00 - 1:30 pm

# Write a function condense_meeting_times() that takes a list of meeting time
# ranges and returns a list of condensed ranges.

# For example, given:

#   [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

# your function would return:

#   [(0, 1), (3, 8), (9, 12)]

# Do not assume the meetings are in order. The meeting times are coming
# from multiple teams.

# In this case the possibilities for start_time and end_time are bounded by the
# number of 30-minute slots in a day. But soon you plan to refactor HiCal to store
# times as Unix timestamps (which are big numbers). Write something that's efficient
# even when we can't put a nice upper bound on the numbers representing our time ranges.

a1 = [(0, 1), (3, 5), (4, 8), (5, 9), (10, 12), (9, 10)]
b1 = [(0, 1), (3, 12)]
a2 = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
b2 = [(0, 1), (3, 8), (9, 12)]

def condense(input_list):

    s = sorted(input_list)
    new_list = []

    # [(0, 1), (3, 5), (4, 8), (9, 10), (10, 12)]
    merged = False
    for i, e in enumerate(s):

        # if 4 <= 5 then merge
        if i+1 > len(s)-1:
            continue

        if s[i+1][0] <= e[1]:
            new_range = (e[0], max(s[i+1][1], e[1]))
            # print new_range
            # before appending to new list check if last in new list can be merged with cur
            if new_range[0] <= new_list[-1][1]:
                new_list[-1] = (new_list[-1][0], new_range[1])
            else:
                new_list.append(new_range)
            merged = True
        elif merged:
            merged = False
            continue
        else:
            new_list.append(e)

    return new_list


def merge_ranges(meetings):

    # sort by start times
    sorted_meetings = sorted(meetings)

    # initialize merged_meetings with the earliest meeting
    merged_meetings = [sorted_meetings[0]]

    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:

        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

        # if the current and last meetings overlap, use the latest end time
        if (current_meeting_start <= last_merged_meeting_end):
            merged_meetings[-1] = (last_merged_meeting_start, max(last_merged_meeting_end, current_meeting_end))

        # add the current meeting since it doesn't overlap
        else:
            merged_meetings.append((current_meeting_start, current_meeting_end))

    return merged_meetings



# assert condense(a1) == b1
# assert condense(a2) == b2
# assert condense(a1) == merge_ranges(a1)
# assert condense(a2) == merge_ranges(a2)











#################################################################
#################################################################
# https://www.interviewcake.com/question/python/coin
#################################################################
#################################################################

# Imagine you landed a new job as a cashier...
# Your quirky boss found out that you're a programmer and has a weird request
# about something they've been wondering for a long time.

# Write a function that, given:

# an amount of money
# a list of coin denominations
# computes the number of ways to make amount of money with coins of
# the available denominations.

# Example: for amount=4 and denominations=[1,2,3], your program
# would output 4-the number of ways to make 4 with those denominations:

# 1, 1, 1, 1
# 1, 1, 2
# 1, 3
# 2, 2

def make_money(amount, denos):

    # if amount % denos[i] == 0, then num++
    # if pairs, then num++
    # if amount-1=x; if amount%x=0, then num++

    num = 0
    combs = []
    for i,e in enumerate(denos):

        # if amount % denos[i] == 0, then num++
        if amount % e == 0:
            print 'h1', [e for _ in range(amount/e)]
            combs.append([e for _ in range(amount/e)])
            num += 1

        # if pairs, then num++
        for j,f in enumerate(denos[i:]):
            if e + f == amount and e != f:
                print 'h2', [e, f]
                combs.append([e,f])
                num += 1

        # if amount-1=x; if amount%x=0, then num++
        diff = amount - e
        for k, g in enumerate(denos[0:i]+denos[i+1:]):
            # diff=2, [1,3]
            if diff % g == 0:
                print 'i', i, 'h3', [e for _ in range(diff/g)]
                combs.append([e for _ in range(diff/g)])
                num += 1


    # print 'total:', num
    # print combs
    return num

make_money(4, [1,2,3])