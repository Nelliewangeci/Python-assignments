#1.Create empty list called my_list
my_list = []

#2.Append my_list with 10,20,30,40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#3.Insert 15 at the second position of the list
my_list.insert(1,15)

#4.Extend my-list with another list(50,60,70)
my_list.extend([50,60,70])

#5.Remove the last element from my_list
my_list.pop()

#6.Sort my_list in ascendind order
my_list.sort()

#7.Find and print the value of the index 30 in my_list
index_30 = my_list.index(30)
print (index_30)
print(my_list)