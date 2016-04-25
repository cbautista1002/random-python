def fib():
  a, b = 0, 1
  while b < 50:
    yield b
    print a, b
    a, b = b, a+b
    print a, b

fib_gen = fib()
for i in fib_gen:
  print 'fib:', i

