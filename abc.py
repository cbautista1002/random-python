import abc

class MyBaseClass(object):

  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def my_abstract_func(self, a, b):
    return

  @abc.abstractmethod
  def to_override(self, x):
    return x**x

  @abc.abstractproperty
  def some_property(self):
    return 'bad'

  def another_prop_get(self):
    return 'badbad'

  def another_prop_set(self, v):
    return

  another_prop = abc.abstractproperty(another_prop_get, another_prop_set)

  @abc.abstractproperty
  def third(self):
    return 'badbadbad'

  @third.setter
  def third(self, v):
    return


class MySubClass(MyBaseClass):

  def __init__(self):
    self._another_prop = 'default'
    self._third = 0

  def my_abstract_func(self, a, b):
    print self, a, b

  def to_override(self, x):
    temp = super(MySubClass, self).to_override(x)
    print 'parents response:', temp

  @property
  def some_property(self):
    return 'good'

  def another_prop_get(self):
    return self._another_prop

  def another_prop_set(self, v):
    self._another_prop = v

  another_prop = property(another_prop_get, another_prop_set)

  @property
  def third(self):
    return self._third

  @third.setter
  def third(self, v):
    self._third = v


class MyRegisteredClass(object):

  def my_abstract_func(self, a, b):
    print self, a, b


# TypeError: Can't instantiate abstract class MyBaseClass with abstract methods
# m = MyBaseClass()
# m.my_abstract_func(1,2)
m = MySubClass()
m.my_abstract_func(1, 2)
m.to_override(5)
print 'm.some_property:', m.some_property
print 'm.another_prop:', m.another_prop
m.another_prop = 'overwritten'
print 'm.another_prop:', m.another_prop
print 'm.third:', m.third
m.third = 'overwritten third'
print 'm.third:', m.third
assert issubclass(MySubClass, MyBaseClass)
assert isinstance(MySubClass(), MyBaseClass)
print 'asserted sub'

MyBaseClass.register(MyRegisteredClass)
assert issubclass(MyRegisteredClass, MyBaseClass)
assert isinstance(MyRegisteredClass(), MyBaseClass)
print 'asserted reg'

# the following only shows subclasses not registered classes
for s in MyBaseClass.__subclasses__():
  print s.__name__