#!/usr/bin/env python3


def knights():
    title = 'Sir'
    action = (lambda x: title + ' ' + x) # title in enclose def scope
    return action                        # return a function object


act = knights()
msg = act('Robin')  # 'Robin passed to x
print(msg)

print(act)  # act:a function, not its result
