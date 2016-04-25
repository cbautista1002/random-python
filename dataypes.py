
def counter():
  from collections import Counter
  a = [1,2,3,1,2,3,4,4,3,2,1,1,2,3,4,1,4,2,2]
  c = Counter(a)
  print 'most_common', c.most_common(1)
  print ''.join(sorted(str(i) for i in c.elements()))
  assert sum(c.values()) == len(a), 'did not match'


def o_dict():
  from collections import OrderedDict
  d = OrderedDict()
  d = dict()
  d['sadfasdfsadfasf'] = 32421
  d['r2wefvgr32wfevd'] = 346
  d['23rwfeavdfgrwef'] = 3987
  d['ghtbrfdvsrgthy'] = 3345
  d['nyj564hwergyj'] = 35632
  print d


def l_checks():
  print [1,2,3,4] == [1,2,3,4] # True
  print [1,2,3,4] == [1,2,4,3] # False
  print [(1,2),(3,4),(5,6)] == [(1,2),(3,4),(5,6)] # True
  print [(1,2),(3,4),(5,6)] == [(1,2),(3,4),(6,5)] # False
  print [(1,2),(3,4),(5,6)] == [(1,2),(5,6),(3,4)] # False


class OneTimeDict(dict):
  def __setitem__(self, k, v):
    if k in self:
      raise Exception, 'too bad, already set'
    else:
      dict.__setitem__(self, k, v)


class FrozenDict(dict):
  def __setitem__(self, k, v):
    raise Exception, 'frozen!'


def otd():
  m = OneTimeDict()
  m['2342'] = 4232
  print m
  m['2342'] = 4232
  print m


def fd():
  m = FrozenDict({'asdf':3})
  # m['2342'] = 4232
  print m
  # m['2342'] = 4232
  # print m

# o_dict()
# l_checks()
# otd()
fd()