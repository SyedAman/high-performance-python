"""
This demonstrates the event loop pattern. It is found in many places to handle asynchrony, such as in NodeJS.

It gets its name because it is a simple while loop that dequeues a queue of callbacks and executes them.
Whenever an asynchronous operation is needed to be performed, such as writing to a db, this operation is
immediately added to a queue to be processed at a later time. This allows subsequent code to be run without
the long-running task of writing to a db from blocking it.

The event loop is a simple way to implement asynchronous IO.
"""

from queue import Queue


class EventLoop(Queue):
    def start(self):
        while True:
            callback = self.get()
            callback()

