def Sort(listofnumbers):
    if len(listofnumbers) > 1:
        tempListLeft = listofnumbers[:len(listofnumbers)//2]
        tempListRight = listofnumbers[len(listofnumbers)//2:]
        
        Sort(tempListLeft)
        Sort(tempListRight)

        i_L = 0
        i_R = 0
        i_list = 0

        while i_L  < len(tempListLeft) and i_R < len(tempListRight):
            if(tempListLeft[i_L] <= tempListRight[i_R]):
                listofnumbers[i_list] = tempListLeft[i_L]
                i_L += 1
            else:
                listofnumbers[i_list] = tempListRight[i_R]
                i_R += 1
            i_list += 1
            

        while i_L < len(tempListLeft):
            listofnumbers[i_list] = tempListLeft[i_L]
            i_L += 1
            i_list += 1
            
        while i_R < len(tempListRight):
            listofnumbers[i_list] = tempListRight[i_R]
            i_R += 1
            i_list += 1

def printList(list):
    for i in range(len(list)):
        print(list[i], end=" ")
    print()