request = ['xyz', 'abc']

def outer(arg):
  def validator(f):
    def decorated():
      if arg in request:
        f()
      else:
        raise Exception, 'denied'
    return decorated
  return validator


# outer return the REAL decorator and passes in the arg
@outer('abcs')
def admin():
  print 'allowing admin something to run'

# admin = validator(admin)

admin()