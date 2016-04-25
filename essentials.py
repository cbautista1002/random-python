# import os


# def print_directory_contents(start_path):

#     for i in os.listdir(start_path):
#         if os.path.isfile(os.path.join(start_path, i)):
#             print 'File: %s' % i
#         else:
#             print 'Directory: %s' % i
#             print_directory_contents(os.path.join(start_path, i))

# def print_directory_contents(sPath):
#     for sChild in os.listdir(sPath):
#         sChildPath = os.path.join(sPath,sChild)
#         if os.path.isdir(sChildPath):
#             print_directory_contents(sChildPath)
#         else:
#             print(sChildPath)

# print_directory_contents('/home')


###################################################################


# A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))

# A0 = {'a':1,'b':2,'c':3,'d':4,'e':5}

# A1 = range(10)

# A1 = [0,1,2,3,4,5,6,7,8,9]

# A2 = sorted([i for i in A1 if i in A0])

# A2 = []

# A3 = sorted([A0[s] for s in A0])

# A3 = [1,2,3,4,5]

# A4 = [i for i in A1 if i in A3]

# A4 = [1,2,3,4,5]

# A5 = {i:i*i for i in A1}

# A5 = {0:0,1:1,2:4,3:9,4:16,5:25,6:36,7:49,8:64,9:81}

# A6 = [[i,i*i] for i in A1]

# A6 = [[0,0],[1,1],[2,4]...]



D B

class A(object):
    def go(self):
        print("go A go!")
    def stop(self):
        print("stop A stop!")
    def pause(self):
        raise Exception("Not Implemented")

class B(A):
    def go(self):
        print 'B'
        super(B, self).go()
        print("go B go!")

class C(A):
    def go(self):
        print 'C'
        super(C, self).go()
        print("go C go!")
    def stop(self):
        super(C, self).stop()
        print("stop C stop!")

class D(B,C):
    def go(self):
        print 'D'
        super(D, self).go()
        print("go D go!")
    def stop(self):
        super(D, self).stop()
        print("stop D stop!")
    def pause(self):
        print("wait D wait!")

class E(B,C): pass

a = A()
b = B()
c = C()
d = D()
e = E()

# specify output from here onwards

# print 'GO:'
# a.go() # go A go!
# print 'GO:'
# b.go() # go A go! \n go B go!
# print 'GO:'
# c.go() # go A go! \n go C go!
print 'GO:'
d.go() # A C B D -- MRO = D-B-A
# print 'GO:'
# e.go() # A C B

# print 'STOP:'
# a.stop() # A
# print 'STOP:'
# b.stop() # A
# print 'STOP:'
# c.stop() # A C
# print 'STOP:'
# d.stop() # A C D
# print 'STOP:'
# e.stop() # A C

# print 'PAUSE:'
# a.pause() # exc
# print 'PAUSE:'
# b.pause() # exc
# print 'PAUSE:'
# c.pause() # exc
# print 'PAUSE:'
# d.pause() # D
# print 'PAUSE:'
# e.pause() # exc




# class A(object):
#     def foo(self,x):
#         print "executing foo(%s,%s)"%(self,x)

#     @classmethod
#     def class_foo(cls,x):
#         print "executing class_foo(%s,%s)"%(cls,x)

#     @staticmethod
#     def static_foo(x):
#         print "executing static_foo(%s)"%x

# a=A()
# # a.foo(1)
# # a.class_foo(2)
# # a.static_foo(3)

# A.foo(6)
# A.class_foo(5)
# A.static_foo(4)



# class First(object):
#     #def __init__(self):
#         # print "first"
#     pass

# class Second(object):
#     def __init__(self):
#         print "second"

# class Third(First, Second):
#     def __init__(self):
#         super(Third, self).__init__()
#         print "that's it"