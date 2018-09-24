#!/usr/bin/env python3

"""Inner Functions
It’s possible to define functions inside other functions.
Such functions are called inner functions. """


def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function.")

    def second_child():
        print("Printing from the second_child() function.")

    second_child()
    first_child()


parent()

"""Furthermore, the inner functions are not defined until the parent function
 is called. They are locally scoped to parent(): they only exist inside the 
 parent() function as local variables. """

#Try calling first_child(). You should get an error:
#first_child()

"""Whenever you call parent(), the inner functions first_child() and second_child()
 are also called. But because of their local scope, they aren’t available outside 
 of the parent() function."""