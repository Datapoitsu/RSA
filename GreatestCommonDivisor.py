## -------------------- Greatest common divisor ------------------------- ##
#Written by: Aarni Junkkala

#Returns the value of the greates common divisor
#Example:  GCD([12,6,15]) -> 3
def GCD(numbers):
    
    ## ----- Return and Fail conditions ----- ##
    
    #Must be a list
    if type(numbers) != list:
        return False
    
    #Null list or list of one value returns false
    if len(numbers) == 0 or len(numbers) == 1:
        return False
    
    #If any of the numbers isn't a integer, then return False
    for i in range(len(numbers)):
        if isinstance(numbers[i], float) or isinstance(numbers[i],int):
            if float(numbers[i]).is_integer() == False:
                return False
        else:
            return False

    ## ----- Removing zeros ----- ##
    # -- How zero really works in GCD -- #
    # GDC(a,0) = a
    # Later on code will return value if it is singular.
    # So zeros will just be removed and result will be good.
    
    #Collects amount of zeros
    ToRemove = 0
    for i in range(len(numbers)):
        if numbers[i] == 0:
            ToRemove += 1
    #Removes all zeros
    for i in range(ToRemove):
        numbers.remove(0)

    ## ----- Singular value returns itself ----- ##
    if len(numbers) == 1:
        return numbers[0]
    
    ## ----- Converts all numbers to positive numbers ----- ##
    for i in range(len(numbers)):
        if numbers[i] < 0:
            numbers[i] *= -1
    
    ## ----- Number one always returns one ----- ##
    # GCD(a,1) = 1
    for i in range(len(numbers)):
        if numbers[i] == 1:
            return 1
    
    ## ----- if all values are same, then just return one of them ----- ##
    # a = b, GCD(a,b) = a || GCD(a,b) = b
    AllSame = True
    for i in range(1,len(numbers)):
        if numbers[0] != numbers[i]:
            AllSame = False
            break
    if AllSame == True:
        return numbers[0]
    
    ## ----- Prosessing the GCD ----- ##
    #Code starts from the lowest number on the list,
    #then tests if it is divisor of all number.
    #If not, then lowers number by one, till divisor of all is found or number becomes one.
    
    #Gets the value with lowest value from the list, as answer will always be <= to that
    Lowest = numbers[0]
    for i in range(1,len(numbers)):
        if numbers[i] < Lowest:
            Lowest = numbers[i]
    
    num = Lowest #Num will be the highest common divisor
    while True:
        #Can't be lower than one
        if num == 1:
            return 1
        for i in range(len(numbers)):
            Failed = False #If is true, means that num isn't divisior of the list
            #if not an integer, then reduce the num and new round
            if (numbers[i] / num).is_integer() == False:
                Failed = True
                break
        if Failed == True: #Lowers num and starts a new round
            num -= 1
            continue
        return num
  
if __name__ == '__main__':
    #Test
    print(GCD([112,98]))
    print(GCD([356,92]))
    print(GCD([0,15,3,0,2]))