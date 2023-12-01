def bubbleSort(list):
    
    exchanges = True
    
    p = len(list)-1
    
    while (p > 0 and exchanges):      
        exchanges = False      
        for i in range(p):       
            if (list[i]>list[i+1]):          
                exchanges = True          
                temp = list[i]          
                list[i] = list[i+1]          
                list[i+1] = temp      
        p = p-1