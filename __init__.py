"""
Part game, part python.
"""

from Queue import Queue
from coroutine import coroutine

class SimObject(object):
    id = 0
    def __init__(self):
        self.ready = Queue()
        self.target = None
        self.sendVal = None
        SimObject.id += 1
        self.id = SimObject.id
        self.task = self.runTarget()
        self.done = False

    def run(self):
        while not self.done:
            yield
            self.task.next()

    @coroutine
    def runTarget(self):
        first = True
        while not self.ready.empty() or self.target or first:
            first = False
            yield
            if self.target:
                try:
                    self.target.send(self.sendVal)
                except StopIteration:
                    self.target = None
            elif not self.ready.empty():
                self.target = self.ready.get_nowait()
                try:
                    self.target.send(self.sendVal)
                except StopIteration:
                    self.target = None


class Scheduler(object):
    def __init__(self):
        self.ready = Queue()
        self.simmap = {}

    def add(self,task):
        self.simmap[task.id] = task

    def schedule(self,task):
        self.ready.put(task)

    def exit(self,task):
        del self.simmap[task.id]

    def mainloop(self):
        while self.simmap:
            task = self.ready.get()
            try:
                task.run()
            except StopIteration:
                self.exit(task)
                continue
            self.schedule(task)


