from collections import Counter

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

counter2 = Counter(list2)
result = []
for num in list1:
    if counter2[num] > 0:
        counter2[num] -= 1
    else:
        result.append(num)

for num in list2:
    if list1.count(num) < list2.count(num):
        result.append(num)

print(result)