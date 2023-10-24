"""
Consider a list (list = []). You can perform the following commands:

1. insert i e: Insert integer e at position i.
2. print: Print the list.
3. remove e: Delete the first occurrence of integer .
4. append e: Insert integer e at the end of the list.
5. sort: Sort the list.
6. pop: Pop the last element from the list.
7. reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands
where each command will be of the 7 types listed above.
Iterate through each command in order and perform the corresponding operation on your list.

Example
N = 4
append 1
append 2
insert 3 1
print
append 1: Append 1 to the list, arr = [1].
append 2: Append 2 to the list, arr = [1,2].
insert 3 1: Insert 3 at index 1 , arr = [1,3,2]
print: Print the array.

Input Format
The first line contains an integer, n, denoting the number of commands.
Each line i of the n subsequente lines contains one of the commands described.
"""
N = int(input())
arr = []

# linhas de comando
for i in range(N):
    linha = input().split(' ')
    if linha[0] == 'insert':
        arr.insert(int(linha[1]), int(linha[2]))
    elif linha[0] == 'append':
        arr.append(int(linha[1]))
    elif linha[0] == 'remove':
        arr.remove((int(linha[1])))
    elif linha[0] == 'sort':
        arr.sort()
    elif linha[0] == 'pop':
        arr.pop()
    elif linha[0] == 'reverse':
        arr.reverse()
    else:
        print(arr)