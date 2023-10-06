num = int(input())
nums = set(range(1, num + 1))
pos_nums = nums
while True:
    X = input()
    if X == 'HELP':
        break
    X = {int(x) for x in X.split()}
    if  len(pos_nums & X) > len(pos_nums) / 2:
        print('YES')
        pos_nums &=X
    else:
        print('NO')
        pos_nums &= nums - X

print(' '.join([str(x) for x in sorted(pos_nums)]))