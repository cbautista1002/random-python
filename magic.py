class Some(object):

  def __init__(self, a, b, c):
    self.a = a*b*c

  def __call__(self, *args, **kwargs):
    print 'called'


s1 = Some( *[1,2,3] )
print s1.a

s1()
