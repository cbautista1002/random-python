
class C(object):

  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c
    self._d = a*b*c

  @property
  def d(self):
    """ asdf """
    print 'getting d'
    return self._d

  @d.setter
  def d(self, val):
    print 'setting d'
    self._d = val

  @d.deleter
  def d(self):
    print 'deleting d'
    del self._d

# c1 = C(1,2,3)
# print c1.d
# c1.d = 234
# print c1.d


def timer(func_to_call):
  def wrapper(*func_to_calls_args):
    t1 = time.time()
    func_to_call(*func_to_calls_args)
    print 'runtime:', time.time()-t1
  return wrapper


import time

class lazy(object):

  def __init__(self, fget):
    self.fget = fget
    self.f_name = fget.__name__

  def __get__(self, obj, cls):
    if obj is None:
      raise Exception, 'Must create object'
    v = self.fget(obj)
    setattr(obj, self.f_name, v)
    setattr(obj, 'asdf', v*v)
    return v

class Test(object):
  # @lazy
  def results(self):
    time.sleep(1)
    return 33333
  results = lazy(results)

t1 = Test()

@timer
def get_r(t, t2):
  print t.results
  print t2


get_r(t1, 1)
get_r(t1, 2)

