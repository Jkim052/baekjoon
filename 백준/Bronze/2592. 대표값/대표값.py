num_list = [int(input()) for _ in range(10)]

ave = sum(num_list)//10

num_dict = {}
most_list = []

for i in num_list:
    if i not in num_dict:
        num_dict[i] = 1
    else:
        num_dict[i] += 1

most = max(num_dict.values())

for key in num_dict.keys():
    if num_dict[key] == most:
        most_list.append(key)




print(ave, most_list[0])