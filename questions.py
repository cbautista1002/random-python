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

assert get_products_of_all_ints_except_at_index([1, 7, 3, 4])    == [84, 12, 28, 21]
assert get_products_of_all_ints_except_at_index([1, 7, 3, 4, 0]) == [0, 0, 0, 0, 84]
print 'asserted'





#################################################################
#################################################################
# https://www.interviewcake.com/question/python/highest-product-of-3
#################################################################
#################################################################

# Given a list_of_ints, find the highest_product you can get from three of the integers.
# The input list_of_ints will always have at least three integers.

a = [1, 7, 3, 4]