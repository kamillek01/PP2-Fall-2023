#Task 4
A = [int(i) for i in input().split()]
for i in range(1, len(A)):
    if A[i - 1] * A[i] > 0:
        print(A[i - 1], A[i])
        break