#WAP to get sum of list items 
#l = [1,2,3,4,5,6,7,8,9]
total = 0
list_num = [1,2,3,4,5,6,7,8,9]
print("length of list is : ",len(list_num))
for ele in range(0,len(list_num)):
    total=total+list_num[ele]
print("sum of all elemnets is - ",total)
print("------------")
#WAP to reverse elments in list
# [10,20,30,40,50]
list_given = [10,20,30,40,50]
print("original list is - ",list_given)
list_rev = []
for num in list_given:
    list_rev.insert(0,num)
print("reversed list is - ",list_rev)
print("------------")
#WAP to merge two list in third list
list1 = [1,2,3,4]
print("list 1 is - ",list1)
list2 = [5,6,7,8]
print("list 2 is - ",list2)
list3 = []
for num in list1:
    list3.insert(3,num)
for num in list2:
    list3.append(num)
print("third list after combining two list is ",list3)
