list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']


#result = [None]*(len(list1)+len(list2))
#result[::2] = list1
#result[1::2] = list2
#print(result)


#res=list(map(list, zip(list1, list2)))
#print(res)


#for x in zip(list1, list2):
#    print(x)


import itertools
print(list(itertools.chain(*zip(list1, list2))))

