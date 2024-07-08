# Declare tuple to store information
# about Book Title, Price, Author,
# pageCount. Store information of any 4
# books in a list and print as below
# Title  Pages Price Author
# ========================================
# Let US C 450 Kanitkar 338
# ....................................... 
te1 = ("twisted hate",356,"ana huang",280.0)
te2 = ("emma",454,"jane auston",2245)
te3 = ("the way we live now",312,"anthony",1245)
te4 = ("let us c",450,"kanitkar",338)

list_book = []
list_book.append(te1)
list_book.append(te2)
list_book.append(te3)
list_book.append(te4)
print("title  pages  price   author")
for i in range(len(list_book)):
    tup = list_book[i]
    print(list_book[i][0],list_book[i][1],list_book[i][2],list_book[i][3])