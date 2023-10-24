"""
Given an integer, n, and n space-separated integers as input, create a tuple,t, of those n integers.
Then compute and print the result of hash(t).
Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

The first line contains an integer, n, denoting the number of elements in the tuple.
The second line contains n space-separated integers describing the elements in tuple .
"""
n = int(input())
integer_list = tuple(map(int, input().split()))
print(hash(integer_list))