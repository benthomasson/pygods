"""
Part game, part python.
"""


class SimObject(object):
    taskid = 0
    def __init__(self):
        self.target = None
        self.sendVal = None

    def run(self):
        if self.target:
            self.target.send(self.sendVal)

from Queue import Queue

class Scheduler(object):
    pass



