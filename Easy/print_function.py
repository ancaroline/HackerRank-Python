"""
Without using any string methods, try to print the following:
123...n
Note that "..." represents the consecutive values in between.
"""
n = int(input())
i = 1
for i in range(1, n+1):
    print(i, end="")