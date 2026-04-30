from threading import Semaphore

class H2O(object):
    __slots__ = ['h_acq', 'h_rel', 'o_acq', 'o_rel', 's_acq', 's_rel']

    def __init__(self):
        h = Semaphore(2)
        o = Semaphore(1)
        s = Semaphore(0)
        
        self.h_acq = h.acquire
        self.h_rel = h.release
        self.o_acq = o.acquire
        self.o_rel = o.release
        self.s_acq = s.acquire
        self.s_rel = s.release

    def hydrogen(self, releaseHydrogen):
        self.h_acq()
        releaseHydrogen()
        self.s_rel()

    def oxygen(self, releaseOxygen):
        self.o_acq()
        self.s_acq()
        self.s_acq()
        releaseOxygen()
        self.h_rel()
        self.h_rel()
        self.o_rel()