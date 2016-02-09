
"""Demonstrate scoping"""

count = 0

def show_count():
    print("count = ", count, ", id = ", id(count))

def set_count(c):
    global count
    count = c

