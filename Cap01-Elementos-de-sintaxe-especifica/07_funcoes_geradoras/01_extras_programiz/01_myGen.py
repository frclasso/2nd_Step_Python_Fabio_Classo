#!/usr/bin/env python3
# A simple generator function


def my_gen():
    n = 1
    print("This is printed first!")
    # Generator functions contains yield statements
    yield n

    n += 1
    print("this is printed second")
    yield n

    n += 1
    print("this is printed last!")
    yield n


# It returns an object but does not start execution immediately.
a = my_gen()
print(next(a)) # We can iterate through the items using next().
# Once the function yields, the function is paused and the control is transferred to the caller.
# Local variables and theirs states are remembered between successive calls.

print(next(a))
print(next(a))
# Finally, when the function terminates, StopIteration is raised
# automatically on further calls.
#print(next(a))
