def rev(s):
    listik = s.split()
    for i in reversed(listik):
        print(i, end = " ")

rev(input())