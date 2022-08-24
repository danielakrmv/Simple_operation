k = int(input())
#if we want random list of numbers
# test_list = [int(x) for x in input().split(', ')]
test_list = [44, 35, 82, 14, 22, 66, 53]
sorted_list = sorted(test_list)[-k:]

kth_max = sorted_list[0]
print(kth_max)


