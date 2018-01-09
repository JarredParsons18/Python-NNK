import ExcelWriter as ew
import threeNumCalc as tnc
import fourNumCalc as fnc

    
def MainLoop(minVal, maxVal, expVal, board, minReq, numQuant, operators, filename):
     



    
    #inserted for large number testing purposes. it's the Fibonacci Board
    #board = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6465, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817]

    numRange = []    
    for i in range(minVal, maxVal +1):
        numRange.append(float(i))
    if expVal == 0:
        expRange = [0, 1]
    else:
        expRange = []
        for i in range(1, expVal +1):
            expRange.append(float(i))
    if numQuant == 3:
        outerDict, innerDict = tnc.ThreeNumCalc(numRange, expRange, minReq, board, operators)
        if len(outerDict) <= 0:
            return 'NoData'
        status = ew.writeVals(outerDict, innerDict, filename, board)
        return True
    else:
        outerDict, innerDict = fnc.FourNumCalc(numRange, expRange, minReq, board, operators)
        if len(outerDict) <= 0:
            return 'NoData'
        status = ew.writeVals(outerDict, innerDict, filename, board)
        return True

  
#inserted for convenience of testing


#filename = 'genericTest'
#operators = ['+', '-', '*', '/']


#inserted for large number testing purposes. it's the Fibonacci Board
#board = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, \
#6465, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, \
# 2178309, 3524578, 5702887, 9227465, 14930352, 24157817]
#MainLoop(1,25, 3, board, 4, 3, operators, filename)

#theEights
#board =  [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, \
#160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256, 264, 272, 280, 296]
#MainLoop(1, 17, 1, board, 4, 4, operators, filename)

#easy board
#board = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#MainLoop(1,10, 1, board, 4, 3, operators, filename)





    
    
    
