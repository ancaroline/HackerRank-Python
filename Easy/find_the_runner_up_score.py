"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
You are given  scores. Store them in a list and find the score of the runner-up.

Input Format
The first line contains n. The second line contains an array A[] of n integers each separated by a space.
"""

n = int(input())
arr = list(map(int, input().split()))

arr.sort()
score = sorted(set(arr))
print(score[-2])