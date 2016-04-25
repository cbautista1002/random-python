
import math, sys

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False


def prime_generator_maker(number):
    print 'here0'
    while True:
        if is_prime(number):
            print 'number:', number
            number = yield number
        number += 1


def print_successive_primes(max_power, base=10):
    print 'here1'
    # this does not execute the generator; it creates the generator object
    prime_generator = prime_generator_maker(base)
    print type(prime_generator)
    print 'here2'
    print prime_generator.send(None)
    print 'here3'
    for power in range(max_power):
        print 'base', base
        print 'power', power
        temp = base ** power
        print 'temp', temp
        print 'prime:', prime_generator.send(temp)


# print_successive_primes(3)


def it_test():
  my_g = (i for i in range(4))
  print next(my_g)
  print 'h'
  # print sys.getsizeof([i for i in range(100)])
  # print sys.getsizeof((i for i in range(100)))

  for i in my_g:
    print i, 'a'
    try:
      print next(my_g), 'b'
    except StopIteration, err:
      print 'err', err
    print next(my_g), 'b'
  else:
    print 'we\'re here'


def remove_from_list(r_or_a):
  a = range(10)
  print a
  c = 0
  for i in a:
    print i
    if r_or_a:
      if i == 5: a.remove(i)
    else:
      # for's internal counter moves up and keeps on seeing i==5
      # i is not the same as for's internal counter
      if i == 5:
        print 'looking at %s, %s, %s' % (i, a[i], a)
        a.insert(i, 'p')
        if c == 3:
          break
        c+=1
  print a

remove_from_list(False)