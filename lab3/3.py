#Task 3
A = [int(i) for i in input().split()]
for i in range(1, len(A)):
    if A[i] > A[i - 1]:
        print(A[i])