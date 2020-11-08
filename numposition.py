q =[[1,3,5], [2, 10, 4], [9, 12,13]]
search_val = int(input("Please input a value : "))

for num_list in q:
    if search_val in num_list:
        print(search_val, "found at pos : ", q.index(num_list), num_list.index(search_val))
        break

for index, num_list in enumerate(q):
    for index2, number in enumerate(num_list):
        
        if number == search_val:
            print(search_val, "found at pos : ", index, index2)