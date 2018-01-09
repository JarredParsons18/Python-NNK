from constraint import *

acceptParenth = ['(_)(_)', '_(__)_', '(___)_', '_(___)', '___(_)', '(_)___']
def parenthRules4(p1,p2,p3,p4,p5,p6):
    try:
        acceptParenth.index(p1+p2+p3+p4+p5+p6)
        return True
    except:
        return False

def parenthRules(p1, p2, p3, p4):
    return (p1 =='(' and p3 == ')' and p2 == '' and p4 == '' ) \
       or (p1 =='' and p3 =='' and p2 == '(' and p4 == ')') \
       or (p1 == '' and  p2 == '' and p3 == '' and p4 == '')


def cleanParen(p):
    if p == '_':
        return ''
    else:
        return p


def OnlyOne4(n1, n2, n3, n4):
    return [n1, n2, n3, n4].count(1) <= 1

def OnlyOne(n1, n2, n3):
    return [n1, n2, n3].count(1) <= 1

    
def getFormulas(operators, four):
    
    if four == True:
        parenthLeft = ['(', '_']
        parenthRight = [')', '_']
    else:
        parenthLeft = ['(', '']
        parenthRight = [')', '']

    problem = Problem()
    problem.addVariable('p1', parenthLeft)
    problem.addVariable('op1', operators)
    problem.addVariable('p2', parenthLeft)
    problem.addVariable('p3', parenthRight)
    problem.addVariable('op2', operators)
    if four == True:
        
        problem.addVariable('p4', parenthLeft)
        problem.addVariable('p5', parenthRight)
        problem.addVariable('op3', operators)
        problem.addVariable('p6', parenthRight)
        problem.addConstraint(parenthRules4, ['p1', 'p2', 'p3', 'p4', 'p5', 'p6'])

    else:
        problem.addVariable('p4', parenthRight)
        problem.addConstraint(parenthRules, ['p1', 'p2', 'p3', 'p4'])
        
    solutions = problem.getSolutions()

    if four == True:
        
        formulaCombos = []
        for solution in solutions:
            tempList = [cleanParen(solution['p1']), '_', '**', '&', solution['op1'], \
                  cleanParen(solution['p2']), '_', '**', '&', cleanParen(solution['p3']), \
                  solution['op2'], cleanParen(solution['p4']), '_', '**', '&', cleanParen(solution['p5']), \
                  solution['op3'], '_', '**', '&', cleanParen(solution['p6'])]
            formulaCombos.append(tempList)
    else:
        formulaCombos = []
        for solution in solutions:
            formulaCombos.append([solution['p1'], '_', '**', '&', solution['op1'], \
                  solution['p2'], '_', '**', '&',  solution['p3'], \
                    solution['op2'], '_', '**', '&', solution['p4']])
    return formulaCombos

def getNumCombs(numRange, expRange, four):
    numProblem = Problem()

    numProblem.addVariable('n1', numRange)
    numProblem.addVariable('n2', numRange)
    numProblem.addVariable('n3', numRange)
    if four == True:
        numProblem.addVariable('n4', numRange)
        numProblem.addVariable('exp4', expRange)
    numProblem.addVariable('exp1', expRange)
    numProblem.addVariable('exp2', expRange)
    numProblem.addVariable('exp3', expRange)

    if four == True:
        numProblem.addConstraint(OnlyOne4, ['n1', 'n2', 'n3', 'n4'])
    else:
        numProblem.addConstraint(OnlyOne, ['n1', 'n2', 'n3'])

    numSolutions = numProblem.getSolutionIter()

    val = numSolutions.next()
    group1 = []
    group2 = []
    group3 = []
    while val != 'fail':
        if four == True:
            try:
                tempList = [val['n1'], val['exp1'], val['n2'], val['exp2'], \
                                   val['n3'], val['exp3'], val['n4'], val['exp4']]
                group1.append(tempList)
                val = numSolutions.next()
            except:
                val = 'fail'
                continue
            try:
                tempList = [val['n1'], val['exp1'], val['n2'], val['exp2'], \
                                   val['n3'], val['exp3'], val['n4'], val['exp4']]
                group2.append(tempList)
                val = numSolutions.next()
            except:
                val = 'fail'
                continue
            try:
                tempList = [val['n1'], val['exp1'], val['n2'], val['exp2'], \
                                   val['n3'], val['exp3'], val['n4'], val['exp4']]
                group3.append(tempList)
                val = numSolutions.next()
            except:
                val = 'fail'
                continue
        else:
            try:
                tempList = [val['n1'], val['exp1'], val['n2'], val['exp2'], \
                                   val['n3'], val['exp3']]
                group1.append(tempList)
                val = numSolutions.next()
            except:
                val = 'fail'

                continue
            try:
                tempList = [val['n1'], val['exp1'], val['n2'], val['exp2'], \
                                   val['n3'], val['exp3']]
                group2.append(tempList)
                val = numSolutions.next()
            except:
                val = 'fail'
                continue
            try:
                tempList = [val['n1'], val['exp1'], val['n2'], val['exp2'], \
                                   val['n3'], val['exp3']]
                group3.append(tempList)
                val = numSolutions.next()
            except:
                val = 'fail'
                continue
    return group1, group2, group3



def MergeDicts(dict1, dict2, dict3):

    result = {}
    result.update(dict1)
    result.update(dict2)
    result.update(dict3)
    return result

def FilterAnswers(outerDict, innerDict, minReq):
    outerSorted = sorted(outerDict.keys())
    for key in outerSorted:
        if len(outerDict[key]) < int(minReq):
           for ans in outerDict[key]:
               innerKey = key, ans
               del innerDict[innerKey]
           del outerDict[key]
    return outerDict, innerDict


