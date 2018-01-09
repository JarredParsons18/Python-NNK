from threading import Thread
import commonFunctions as cf
import time
import Calc as c
class Threads(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs, Verbose)
        self._return = None
    def run(self):
        if self._Thread__target is not None:
            self._return = self._Thread__target(*self._Thread__args,
                                                **self._Thread__kwargs)
    def join(self):
        Thread.join(self)
        return self._return

def StartThreads(formulaCombos, group1, group2, group3, board, minReq, four):
    t1 = Threads(name='t1', target=c.ProcessNumbers, args=(formulaCombos, group1, board, four))
    t2 = Threads(name='t2', target=c.ProcessNumbers, args=(formulaCombos, group2, board, four))
    t3 = Threads(name='t3', target=c.ProcessNumbers, args=(formulaCombos, group3, board, four))
    t1.start()
    t2.start()
    t3.start()
    dict1, inDict1 = t1.join()
    dict2, inDict2 = t2.join()
    dict3, inDict3 = t3.join()
   # while t1.isAlive() or t2.isAlive() or t3.isAlive():
     #   time.sleep(3)
    outerDict, innerDict = cf.MergeDicts(dict1, dict2, dict3, inDict1, inDict2, inDict3)
    outerDict, innerDict = cf.FilterAnswers(outerDict, innerDict, minReq)
    return outerDict, innerDict
