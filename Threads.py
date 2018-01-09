from threading import Thread
import commonFunctions as cf
import time
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
    if four == True:
        import fourNumCalc as fnc
        t1 = Threads(target=fnc.ProcessNumbers, args=(formulaCombos, group1, board))
        t2 = Threads(target=fnc.ProcessNumbers, args=(formulaCombos, group2, board))
        t3 = Threads(target=fnc.ProcessNumbers, args=(formulaCombos, group3, board))
    else:
        import threeNumCalc as tnc
        t1 = Threads(target=tnc.ProcessNumbers, args=(formulaCombos, group1, board))
        t2 = Threads(target=tnc.ProcessNumbers, args=(formulaCombos, group2, board))
        t3 = Threads(target=tnc.ProcessNumbers, args=(formulaCombos, group3, board))
    t1.start()
    t2.start()
    t3.start()
    dict1, inDict1 = t1.join()
    dict2, inDict2 = t2.join()
    dict3, inDict3 = t3.join()
        
    outerDict = cf.MergeDicts(dict1, dict2, dict3)
    innerDict = cf.MergeDicts(inDict1, inDict2, inDict3)
    outerDict, innerDict = cf.FilterAnswers(outerDict, innerDict, minReq)
    return outerDict, innerDict
