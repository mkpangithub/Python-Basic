totalrows =  int (input("Enter the Number of Row : "))

for  rowno in range(1, totalrows+1):
    for colno in range(1, totalrows+1):
       if (colno == 1) or (rowno == totalrows) or (colno == rowno):
         print(rowno , end=" ")
    else: 
        print(" ", end= " ")


    print()    