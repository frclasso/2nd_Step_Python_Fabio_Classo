class myClass:
    """This is my second class."""
    a = 10

    def func(self):
        print('Hello.')

# output 10
print(myClass.a)

# output <function myClass.func at 0x7fbe224490d0>
print(myClass.func)

# output 'This is my second class'
print((myClass.__doc__))