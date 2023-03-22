import asyncio
from queue import Queue


class EventLoop(Queue):
    def start(self):
        while True:
            callback, args = self.get()
            callback(*args)


if __name__ == '__main__':
    eventloop = EventLoop()

    eventloop.put((print, ('Hello World',)))
    eventloop.put((print, ('another message',)))
    eventloop.put((add := lambda x, y: print(x + y), (1, 2)))

    def concat(*args):
        res = ''.join(args)
        print(res)
        return res

    eventloop.put((concat, ('a', 'b', 'c')))
    eventloop.put((print, ('finished',)))

    eventloop.start()
