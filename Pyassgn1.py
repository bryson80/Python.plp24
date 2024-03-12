# empty list
my_list = []
#Append to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
#insert 15 at second position
my_list.insert(1, 15)
#Extend my_list with another list
my_list.extend([50, 60, 70])
#remove last element form the list
my_list.pop()
#sort my list in ascending order
my_list.sort()
index_of_30 =my_list.index(30)
print("index value of 30:", index_of_30)
#modified list
print("modified list:", my_list)
