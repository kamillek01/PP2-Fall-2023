list=[int(i) for i in input().split()]
list1=[int(i) for i in input().split()]
com_num=sorted(set(list) & set(list1))
for num in com_num:
    print(num)