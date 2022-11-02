from math import sin


class FunctionCaller(object):

    def __init__(self, fun):
        self.fun = fun
        self.arglist = []

    def append_job(self, arg):
        return self.arglist.append(arg)

    def call(self):
        for arg in self.arglist:
            print(f"Calling for job {arg}. Result {self.fun(arg)}")
        if len(self.arglist) == 0:
            print("Nothing to do")    
        self.arglist.clear()    
            
caller = FunctionCaller(sin)
caller.append_job(0)
print(caller.arglist)
caller.append_job(1)
print(caller.arglist)
caller.append_job(3.1415)
print(caller.arglist)
caller.call()
print(caller.arglist)
caller.call()
print(caller.arglist)

