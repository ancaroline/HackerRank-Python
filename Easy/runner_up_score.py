"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
You are given  scores. Store them in a list and find the score of the runner-up.

Input Format
The first line contains n. The second line contains an array A[] of n integers each separated by a space.
"""
from random import randint

n = int(input())

list_run = []

for i in range(n):
    result = randint(2, 10)
    list_run.append(result)
    list_run.sort()

score_second = list_run[n-1]
print(score_second)