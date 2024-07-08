# # to get the secong highest number on the list
# list1 = []
# for i in range(5):
#     data = int(input("Enter a number"))
#     list1.append(data)
# for a in range(len(list1)):
#     for b in range(a+1,len(list1)):
#         if list1[a]<list1[b]:
#             temp = list1[a]
#             list1[a]=list1[b]
#             list1[b]=temp
# print(list1)

# print("the second highest number on list is - ",list1[1])


# 2d array
r1 = [1,2,3]
r2 = [4,5,6]
r3 = [7,8,9]
array1 = [r1,r2,r3]
r4 = [7,8,9]
r5 = [1,2,3]
r6 = [5,6,7]
array2 = [r4,r5,r6]
print("the first array is - ",array1)
print("the second array is - ",array2)
array3=[]
for x in range(len(array1)):
    row=[]
    for y in range(len(array2)):
        row.append(array1[x][y]+array2[x][y])
    array3.append(row)
        
print(array3)
