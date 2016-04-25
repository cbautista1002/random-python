from collections import Counter
from collections import OrderedDict


def counter():
  print 'counter():\n'
  a = [1,2,3,1,2,3,4,4,3,2,1,1,2,3,4,1,4,2,2]
  c = Counter(a)
  print c
  print 'most_common:', c.most_common(1)
  print 'elements:', c.elements()
  print 'join:', ''.join(sorted(str(i) for i in c.elements()))
  assert sum(c.values()) == len(a), 'did not match'
  print '\n\n'

def o_dict():
  d = OrderedDict()
  d = dict()
  d['sadfasdfsadfasf'] = 32421
  d['r2wefvgr32wfevd'] = 346
  d['23rwfeavdfgrwef'] = 3987
  d['ghtbrfdvsrgthy'] = 3345
  d['nyj564hwergyj'] = 35632
  print d

  # regular unsorted dictionary
  d = {'banana': 3, 'apple':4, 'pear': 1, 'orange': 2}

  # dictionary sorted by key
  s = sorted(d.items(), key=lambda t: t[0])
  print OrderedDict(s)


def l_checks():
  print [1,2,3,4] == [1,2,3,4] # True
  print [1,2,3,4] == [1,2,4,3] # False
  print [(1,2),(3,4),(5,6)] == [(1,2),(3,4),(5,6)] # True
  print [(1,2),(3,4),(5,6)] == [(1,2),(3,4),(6,5)] # False
  print [(1,2),(3,4),(5,6)] == [(1,2),(5,6),(3,4)] # False


class OneTimeDict(dict):
  def __setitem__(self, k, v):
    if k in self:
      raise Exception, 'already set'
    else:
      dict.__setitem__(self, k, v)


class FrozenDict(dict):
  def __setitem__(self, k, v):
    raise Exception, 'frozen!'


class OrderedCounter(Counter, OrderedDict):
  'Counter that remembers the order elements are first encountered'
  # pass
  def __repr__(self):
      return '%s(%r)' % (self.__class__.__name__, OrderedDict(self))

  # def __reduce__(self):
  #     return self.__class__, (OrderedDict(self),)


def otd():
  m = OneTimeDict()
  m['2342'] = 4232
  print m
  m['2342'] = 4232
  print m


def fd():
  m = FrozenDict({'asdf':3})
  m['2342'] = 4232
  print m
  # m['2342'] = 4232
  # print m


def oc():
  print 'oc():\n'
  a = [1,4,1,5,3,4,4,3,2,1,1,2,3,4,1,4,2,2]
  o = OrderedCounter(a)
  print o
  for k in o:
    print k
  print '\n\n'

# counter()
o_dict()
# l_checks()
# otd()
# fd()
# oc()