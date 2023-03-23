def simple_generator():
    """Including a yield converts a function into a generator. It allows for pausing
    and resuming execution of a function."""
    yield 1
    yield 2
    yield 3


def drive_simple_generator():
    """Generators return a generator object. You can iterate through a generator object using a for loop."""
    for i in simple_generator():
        print(i)


def drive_simple_generator_with_next():
    """You can iterate over a generator object using next()."""
    generator_object = simple_generator()

    print(next(generator_object))
    print(next(generator_object))
    print(next(generator_object))


def fibonacci(limit):
    """This is a generator that yields a fibonacci sequence up to the limit.
    You can think of this as a stream of fibonacci numbers. You can use it
    without knowing when the stream will end."""
    a, b = 0, 1

    while a < limit:
        yield a
        a, b = b, a + b


def drive_fibonacci_generator():
    fibonacci_generator = fibonacci(10)

    print(next(fibonacci_generator))
    print(next(fibonacci_generator))
    print(next(fibonacci_generator))
    print(next(fibonacci_generator))
    print(next(fibonacci_generator))

    for i in fibonacci_generator:
        print(i)


def file_reader(file_name):
    """This is a generator that yields lines from a file. It can read giant files
    without loading the entire file into memory, neither crashing the program due to
    memory constraints because it yields one line at a time."""
    with open(file_name) as f:
        for line in f:
            yield line


def read_hadoop_file_lines(limit):
    hadoop_log_generator = file_reader('sample-hadoop-log-file.log')
    for line in range(limit):
        print(next(hadoop_log_generator))


def file_writer(file_name):
    """Similar to file_reader, this is a generator that writes lines to a file.
    Except you can send lines to it."""
    with open(file_name, 'w') as f:
        while True:
            line = yield
            f.write(line)


if __name__ == '__main__':
    drive_simple_generator()

    drive_simple_generator_with_next()

    drive_fibonacci_generator()

    read_hadoop_file_lines(10)

    file_writer_generator = file_writer('db.txt')
    next(file_writer_generator)
    file_writer_generator.send('Hello World\n')
    file_writer_generator.send('Goodbye World')
