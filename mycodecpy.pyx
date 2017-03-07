cdef extern from "mycode.h":
    cdef int myfunc (int, int)

def callCfunc ():
    print "Hello"
    print myfunc (1,2)

