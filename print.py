
def eliminate( numbers,n ):
    endLoop = False
    num = 0
    new_number = []
    #dictionary to store the time of a number appears in the array
    dictionary = dict([])
    for i in range(0,len(numbers)):
        #if the number found in dictionary, increase the count
        if numbers[i] in dictionary.keys():
            count = dictionary[numbers[i]]
            count = count + 1
            dictionary[numbers[i]] = count
            if count != n:
                new_number.append(numbers[i])
            
        #if the number is not in the dictionary, add this number to dictionary with the value is 1        
        else:
            count = 1
            dictionary[numbers[i]] = count
            new_number.append(numbers[i])

    print dictionary
    print new_number   
numlist = [1, 2, 2, 3, 5, 2, 4, 5, 5, 2]
eliminate( numlist,3 )
numlist2 = [1,1,2,2,1,2,3,3,4,4,5,5]
eliminate(numlist2,2)

