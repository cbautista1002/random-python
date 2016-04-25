
def is_even(value):
    """ Return True if *value* is even.
        >>> is_even(3)
        False
        >>> is_even(987234)
        True
    """
    return (value % 2) == 0

def count_occurrences(target_list, predicate):
    """ Return the number of times applying the callable
       *predicate* to a list element returns True.
       >>> count_occurrences([1,2,3,4,5], is_even)
       2
       >>> count_occurrences([2, 4, 6, 7, 9, 14], is_even)
       4
    """
    return sum(1 for e in target_list if predicate(e))


import time
def perf(f):
  def perfed():
    t1 = time.time()
    f()
    print 'runtime: {}'.format(time.time() - t1)
  return perfed

@perf
def file_write():
  fh = open('large.txt', 'a')
  for i in xrange(10000000):
    fh.write(str(i)+'\n')
  fh.close()

file_write()
import os
print os.path.getsize('./large.txt')


class C(object):
  def __init__(self):
    self.a = 999
  def __str__(self):
    return str(self.a)
  def __repr__(self):
    return str(self.a)

c1 = C()
print hex(id(c1))
print c1

t = (c1, c1)
d = {t:234}

print t
print hash(t)
print d

c1.a = 111
print t
print hash(t)
print d

c2 = C()

c1 = c2
print hex(id(c1))

print t
print hash(t)
print d

c1.a = 333

print t
print hash(t)
print d