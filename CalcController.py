import ExcelWriter as ew
import threeNumCalc as tnc
import fourNumCalc as fnc

    
def MainLoop(minVal, maxVal, expVal, board, minReq, numQuant, operators, filename):
     



    
    #inserted for large number testing purposes. it's the Fibonacci Board
    #board = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6465, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817]

    numRange = []    
    for i in range(minVal, maxVal +1):
        numRange.append(float(i))
    expRange = []
    for i in range(1, expVal +1):
        expRange.append(float(i))
    if numQuant == 3:
        outerDict, innerDict = tnc.ThreeNumCalc(numRange, expRange, minReq, board, operators)
        status = ew.writeVals(outerDict, innerDict, filename)
        return True
    else:
        outerDict, innerDict = fnc.FourNumCalc(numRange, expRange, minReq, board, operators)
        status = ew.writeVals(outerDict, innerDict, filename)
        if status == 'failedFileName':
            return 'noFileName'
        return True

  
#inserted for convenience of testing

'''
board = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
filename = 'genericTest'
operators = ['+', '-', '*', '/']
MainLoop(1,10, 1, board, 0, 3, operators, filename)
'''





    
    
    
