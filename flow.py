import queue
from math import sin
from threading import Thread
from time import sleep
from random import randint

class Receiver(Thread):
    def __init__(self, queue_, fun):
        self.fun = fun
        self.queue= queue_
        self.senders= []     
        
        def func(g, q):
            for flow in self.senders:
                while flow.is_alive():
                    if q.empty() == False:
                        x=q.get_nowait()
                        print(f" f({x}) = {g(x)}")
                        
        super().__init__(target=func, args=(self.fun, self.queue))
        
    def add_sender(self, sender):
        self.senders.append(sender)                    
                    
                    
class Sender(Thread):   
    def __init__(self, queue_, p, receiver_):
        self.queue = queue_
        self.receiver = receiver_
        
        def func(q):
            for i in range(p):
                sleep(randint(0,7))
                x=randint(-100,100)
                q.put_nowait(x)
                print(f"Sender send {x} -->")
                
        super().__init__(target=func, args=(self.queue, ))
        self.receiver.add_sender(self)        
                
q=queue.Queue(20)
r=Receiver(q, sin)
for i in range(10):
    s=Sender(q, 2, r)
    s.start()
r.start()                    
