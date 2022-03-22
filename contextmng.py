from contextlib import contextmanager


with open('notes.txt', 'w') as file:
    file.write('some todo...')


file = open('notes.txt', 'w')
try:
    file.write('some todo....')
finally:
    file.close()


class ManagedFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print('exception has been handled')
        #print('exec:', exc_type, exc_value)
        print("exit")
        return True


with ManagedFile('notes.txt') as file:
    print("Do something now")
    file.write('some to doo....')
    file.somemethod()
print("continuing")


@contextmanager
def open_managed_file(filename):
    f = open(filename, 'w')
    try:
        yield f
    finally:
        f.close()


with open_managed_file('notes.txt') as f:
    f.write('some todooo....')



