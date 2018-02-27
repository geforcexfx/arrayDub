
def eliminate( numbers ):
    endLoop = False
    num = 0
    new_number = []
    dictionary = dict([])
    for i in range(0,len(numbers)):
        
        if numbers[i] in dictionary.keys():
            count = dictionary[numbers[i]]
            count = count + 1
            dictionary[numbers[i]] = count
            if count < 3:
                print numbers[i]
                new_number.append(numbers[i])
                dictionary[numbers[i]] = 1
                
        else:
            count = 1
            dictionary[numbers[i]] = count
            print numbers[i]
            new_number.append(numbers[i])

    print dictionary
    print new_number
numlist = [1, 2, 2, 3, 5, 2, 4, 5, 5, 2]
eliminate( numlist )

#Output: [1, 2, 2, 3, 5, 4, 5, 2]
