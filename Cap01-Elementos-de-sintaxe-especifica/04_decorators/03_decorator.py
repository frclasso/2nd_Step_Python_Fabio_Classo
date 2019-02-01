#!/usr/bin/env python3


def is_called():
    def is_returned():
        print("Hello")
    return is_returned


new = is_called()
new()