"""

"""

import time
from functools import partial

from event_loop import EventLoop


def save_result_to_db(result):
    print(f"Saving {result} to db")

    with open('generators/db.txt', 'w') as f:
        # sleep for 1 second to simulate db write
        time.sleep(1)

        f.write(result)
        print(f"Saved {result} to db")

    return result


async def save_value(value):
    print(f"Saving {value} to database")
    db_response = await save_result_to_db(value)
    print(f"Response: {db_response}")


if __name__ == '__main__':
    event_loop = EventLoop()
    event_loop.put(partial(save_value, 'xyz'))
    event_loop.start()
