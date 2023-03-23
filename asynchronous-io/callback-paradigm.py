"""
This demonstrates
"""
import time
from functools import partial

from event_loop import EventLoop


def save_result_to_db(result, callback):
    print(f"Saving {result} to db")

    with open('generators/db.txt', 'w') as f:
        time.sleep(1)

        f.write(result)
        print(f"Saved {result} to db")

    callback(result)


def save_value(value, callback):
    print(f"Saving {value} to base")
    save_result_to_db(value, callback)


def print_response(db_response):
    print(f"Response: {db_response}")


if __name__ == '__main__':
    event_loop = EventLoop()

    event_loop.put(partial(save_value, 'xyz', print_response))

    event_loop.start()
