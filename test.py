#!/usr/bin/env python

import unittest
import pygods
from coroutine import coroutine


class SimTest(pygods.SimObject):
    @coroutine
    def foo(self):
        while True:
            x = yield
            print x

    @coroutine
    def bar(self):
        yield
        print "done"

class TestYield(unittest.TestCase):

    def testObject(self):
        sim = pygods.SimObject()
        r = sim.runTarget()
        self.assertRaises(StopIteration,r.next)

    def testSim(self):
        sim = SimTest()
        sim.target = sim.foo()
        r = sim.runTarget()
        r.next()

    def testReady(self):
        sim = SimTest()
        sim.ready.put(sim.foo())
        r = sim.runTarget()
        r.next()

    def testFinished(self):
        sim = SimTest()
        sim.ready.put(sim.bar())
        r = sim.runTarget()
        self.assertRaises(StopIteration,r.next)



if __name__ == '__main__':
    unittest.main()

