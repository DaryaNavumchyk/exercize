list_s = [1, 2, 3, 4, 5, 6, 7]
list_f = []

count = 0

for i in list_s:
    if count % 2 == 0:
        list_f.append(i)
    count += 1
    
print(list_f)