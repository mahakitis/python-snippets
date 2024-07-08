# '''
# * * * *
# * * * *
# * * * *
# * * * *
# '''
# for row in range(4):
#     for col in range(4):
#         print("*",end = " ")
#     print()

# '''
# * 
# * * 
# * * * 
# * * * *
# '''
# for row in range(4):
#     for col in range(row+1):
#         print("*",end = " ")
#     print()

# '''
#       *
#     * *
#   * * *
# * * * *
# '''
# for row in range(5,0,-1):
#     for spaces in range(row-1):
#         print(" ",end=" ")
#     for col in range(row,5):
#             print("*",end=" ")
#     print()
# '''
#           *
#        *  *  *
#     *  *  *  *  *
#  *  *  *  *  *  *  *
# '''
# for row in range(5,0,-1):
#     for spaces in range(row-1):
#         print(" ",end=" ")
#     for col in range(row,5):
#             print("*",end=" ")
#     for col in range(row,4):
#            print("*",end = " ")
#     print()

'''
          *
       *  *  *
    *  *  *  *  *
 *  *  *  *  *  *  *
    *  *  *  *  *
       *  *  *
          *
'''
for row in range(5,0,-1):
    for spaces in range(row-1):
            print(" ",end=" ")
    for col in range(row,6):
            print("*",end=" ")
    for col in range(row,5):
            print("* ", end="")
    print()
for row in range(2,6):
    for spaces in range(row-1):
            print(" ",end=" ")
    for col in range(row,6):
            print("*",end=" ")
    for col in range(row,5):
            print("* ", end="")
    print()