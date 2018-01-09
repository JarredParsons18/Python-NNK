#import required files and packages
import Threads as th
import commonFunctions as cf
import re
import copy

def ThreeNumCalc(numRange, expRange, minReq, board, operators):
    formulaCombos = cf.getFormulas(operators, False)
    group1, group2, group3 = cf.getNumCombs(numRange, expRange, False)
    outerDict, innerDict = th.StartThreads(formulaCombos, group1, group2, group3, board, minReq, False)
    return outerDict, innerDict

def ProcessNumbers(formulaCombos, numCombos, board):

    
    outerDict = {}
    innerDict = {}
    numRegex = r"(\d*).0\*\*"
    expRegex = re.compile(r"\*\*")
    for item in numCombos:
        for cmb in formulaCombos:
            tmp = copy.copy(cmb)
            tmp[tmp.index('_')] = str(item[0])
            tmp[tmp.index('&')] = str(item[1])
            tmp[tmp.index('_')] = str(item[2])
            tmp[tmp.index('&')] = str(item[3])
            tmp[tmp.index('_')] = str(item[4])
            tmp[tmp.index('&')] = str(item[5])
            try:
                
                stringFunc = ''.join(tmp)
                answer = eval(stringFunc)
                if answer in board:
                    nums = re.findall(numRegex, stringFunc)
                    nums.sort()
                    tmpList = []
                    stringFunc = expRegex.sub('^', stringFunc)
                    for val in nums:
                        tmpList.append(val)
                    outerKey = tuple(tmpList)
                    innerKey = outerKey, answer
                    if outerKey in outerDict:
                        if answer in outerDict[outerKey]:
                            innerDict[innerKey].append(stringFunc)
                        else:
                            outerDict[outerKey].append(answer)
                            innerDict[innerKey] = []
                            innerDict[innerKey].append(stringFunc)
                            print stringFunc
                    else:
                        outerDict[outerKey] = []
                        outerDict.append(answer)

            except:
                continue
    return outerDict, innerDict
