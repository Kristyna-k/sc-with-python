#Create a function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to True, the answers should be displayed.

import re

def arithmetic_arranger(lst, result = None):
    if len(lst) > 5:           #error too many numbers   
        print('Error: Too many problems.')
        return
     
    
        

    lenght = []
    numb = []
    op = []

    for a in lst:
        #print(a)

        if (len(a[0]) > 4 or len(a[2]) > 4):             #error long numbers
            print('Error: Numbers cannot be more than four digits.')
            return

        if (re.search('[a-z]+', a)):        #error letters
            print('Error: Numbers may only contain digits.') 
            return  

        if (re.search('\*', a)):          #error just plus or minus
            print('Error: Operator must be \'+\' or \'-\'.')
            return 

        if (re.search('\\\\', a)):          #error just plus or minus
            print('Error: Operator must be \'+\' or \'-\'.')
            return 

        num = a.split()         #separate numbers and operator
        #print(num[0] + ',' + num[1] + ',' + num[2])
        lenght.append(len(num[0]))
        lenght.append(len(num[2]))
        numb.append(num[0])
        numb.append(num[2])
        op.append(num[1])

    
    #print(max(lenght), lenght)
    mlenght = max(lenght)            #determine the lenght of the longest number
   
    #this is definitely not the right way to do it
    #but why go the easy way, when you can go the hard way

    #print(mlenght)
    #print(numb)

    numb_1 = []
    numb_2 = []           #dividing lower and upper line
    
    for i in range (len(numb)):
        if i in [0, 2, 4, 6]:
            numb_1.append(numb[i])
        else:
            numb_2.append(numb[i])


    #print(numb_1)
    #print(numb_2)
    #print(op)
    res = []            #list of results


    for i in range (len(numb_1)):
        dif = (len(numb_1[i]) - len(numb_2[i])) 
        #print(dif)

        if op[i] == '-':
            res.append(int(numb_1[i]) - int(numb_2[i]))            
        else: 
            res.append(int(numb_1[i]) + int(numb_2[i]))
 
        if dif == 0:
            numb_1[i] = '  ' + numb_1[i]            #adding spaces 
            numb_2[i] = op[i] + ' ' + numb_2[i]
        elif dif == 1:
            numb_1[i] = '  ' + numb_1[i]
            numb_2[i] = op[i] + '  ' + numb_2[i]
        elif dif == 2:
            numb_1[i] = '  ' + numb_1[i]
            numb_2[i] = op[i] + '   ' + numb_2[i]
        elif dif == 3:
            numb_1[i] = '  ' + numb_1[i]
            numb_2[i] = op[i] + '    ' + numb_2[i]
        elif dif == -1:
            numb_1[i] = '   ' + numb_1[i]
            numb_2[i] = op[i] + ' ' + numb_2[i]
        elif dif == -2:
            numb_1[i] = '    ' + numb_1[i]
            numb_2[i] = op[i] + ' ' + numb_2[i]
        elif dif == -3:
            numb_1[i] = '     ' + numb_1[i]
            numb_2[i] = op[i] + ' ' + numb_2[i]


    for i in range (len(numb_1)):
        if i == len(numb_1)-1:
            print(numb_1[i])
        else:
            print(numb_1[i], '    ', end='')

    for i in range (len(numb_2)):
        if i == len(numb_1)-1:
            print(numb_2[i])
        else:
            print(numb_2[i], '    ', end='')

    for i in range (len(numb_2)):
        if i == len(numb_1)-1:
            print('_'*(len(numb_2[i])))
        else:
            print('_'*(len(numb_2[i])), '    ', end='')

    if result == True:          #adding results if true
        for i in range(len(res)):
            res[i] = str(res[i])
            print(' '*(len(numb_2[i]) - len(res[i]) - 1), res[i], '    ', end='')


    
