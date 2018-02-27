
def dosomething( numbers ):
    endLoop = False
    dig = 0
    for i in range(0,len(numbers)):
        
        if numbers[i]==numbers[i+1] and i != i+1:
            print numbers
            print numbers[i]
            dig = dig +1
            if dig ==3:
                print numbers[i]
                print "Index"
                print i
                endLoop=True
        if endLoop:
            break


alist = [4,5,1,2,2,2,3,3,3]
dosomething( alist )  
