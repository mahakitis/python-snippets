mark = int(input("enter the mark - "))
if mark>=90 and mark<=100:
    print("A GRADE")
elif mark>=80 and mark<90:
    print("B GRADE")
elif mark>=70 and mark<80:
    print("C GRADE")
elif mark>=60 and mark<70:
    print("D GRADE")
elif mark<60:
    print("E GRADE")
else:
    print("invalid")