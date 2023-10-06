num = int(input())
nums = set(range(1, num + 1))
pos_nums = nums
while True:
    guess = input()
    if guess == 'HELP':
        break
    guess = {int(x) for x in guess.split()}
    answer = input()
    if answer == 'YES':
        pos_nums &= guess
    else:
        pos_nums &= nums - guess

print(' '.join([str(x) for x in sorted(pos_nums)]))