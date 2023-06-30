list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

new_list=[]

min_length = min(len(list1), len(list2))

for i in range(min_length):
    new_list.append(list1[i] + list2[i])

if len(list1) > min_length:
    new_list.extend(list1[min_length:])
elif len(list2) > min_length:
    new_list.extend(list2[min_length:])

print(new_list)