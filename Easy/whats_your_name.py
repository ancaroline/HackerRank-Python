"""
You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:

Hello firstname lastname! You just delved into python.
"""


def print_full_name(f, l):
    return print(f'Hello {f} {l}! You just delved into python.')


first = input()
last = input()
print(print_full_name(first, last))