
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]

result = [None]*(len(list1)+len(list2))
result[::2] = list1
result[1::2] = list2[0]
print(result)
