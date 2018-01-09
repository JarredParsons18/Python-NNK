import Tkinter as tk
import tkMessageBox as tkm
import ttk
import datetime
import CalcController as cc

Queue = []
def compileVariables():
        if len(Queue) > 0:
                quest = tkm.askquestion('Queue exists', \
                               'Would you like to execute the Queue? If not, execute single board')
                        
                if quest == 'yes':
                        result = AddToQueue()
                        if result == "BoardFail" or result == 'FileFail':
                                return
                        StartQueue()
                        return
                   
        board = compileBoard()
        if board == 'BoardFail':
                return
        opVars = [subVal, addVal, multVal, divVal]
        operators = getOperators(opVars)
        filename = getFileName()
        if filename == '':
                tkm.showinfo("Error", "Didn't Enter valid Filename, do not include file extensions, cannot be empty")
                return
        timeBegan = datetime.datetime.now()
        minVal, maxVal, expVal, minReq, numQuant = compileNumVals()
        result = cc.MainLoop(minVal, maxVal, expVal, board, minReq, numQuant, operators, filename)
        if result == 'NoData':
                tkm.showinfo("Error", "There are no answers with this criteria, Try decreasing Min Req, or increase available numbers.")
                return

                

        timeEnd = datetime.datetime.now()
        lapse = timeEnd - timeBegan
        tkm.showinfo('Finished', 'process Finished, time taken: '+str(lapse))

def AddToQueue():
        result = []
        opVars = [subVal, addVal, multVal, divVal]
        minVal = int
        maxVal = int
        expVal = int
        board = []
        minReq = int
        numQuant = int
        operators = int
        filename = str

        minVal, maxVal, expVal, minReq, numQuant = compileNumVals()
        board = compileBoard()
        if board == 'BoardFail':
                return
        filename = getFileName()
        if filename == '':
                tkm.showinfo("error", "Please specify where you'd like the file")
                return 'FileFail'
        operators = getOperators(opVars)
        result = [minVal, maxVal, expVal, board, minReq, numQuant, operators, filename]
        Queue.append(result)
        qCount.set(qCount.get() +1)
        ClearScreen()
        return

def ClearQueue():
        del Queue[:]


def StartQueue():
        
        for order in Queue:
                cc.MainLoop(order[0], order[1], order[2],order[3], order[4], order[5], order[6], order[7])
        qCount.set(0)
        
        ClearQueue()

def ClearBoard():
        #Tkinter is stupid. Don't delete this, even though it's lazy.
        ClearScreen()
                
        
        
    
    

root = tk.Tk()
qCount = tk.IntVar(0)
root.title = 'National Number Knockout'

EntryFrame = ttk.Frame(root, padding="1 1 2 2")
EntryFrame.grid(column=0, row=0)

minlabel = tk.Label(EntryFrame, text="Min Num")
minlabel.grid(column=0, row=0)

minField = tk.Spinbox(EntryFrame, from_=1, to=1000)
minField.grid(column=1, row=0)

maxlabel = tk.Label(EntryFrame, text="Max Num")
maxlabel.grid(column=0, row=1)

maxField = tk.Spinbox(EntryFrame, from_=10, to=1001)
maxField.grid(column=1, row=1)

explabel = tk.Label(EntryFrame, text="Max Exponent")
explabel.grid(column=2, row=0)

expField = tk.Spinbox(EntryFrame, from_=0, to=25)
expField.grid(column=3, row=0)

reqLabel = tk.Label(EntryFrame, text="Min Req Answers")
reqLabel.grid(column=2, row=1)

minNum = tk.Spinbox(EntryFrame, from_=0, to=40)
minNum.grid(column=3, row=1)



numQuant = tk.IntVar()
numQuant.set(3)
numQuantchk = tk.Checkbutton(EntryFrame, text="4 Digits", onvalue="4", offvalue="3", variable=numQuant)
numQuantchk.grid(column=4, row=1)

enterButton = tk.Button(EntryFrame, text="Enter", height=3, width = 6, command=compileVariables)
enterButton.grid(column=5, row=0, rowspan=2, columnspan=2)



BoardLabel = tk.Label(root, text="Enter Board Values below. Leave unneeded spaces blank")
BoardLabel.grid(column=0, row=1)

BoardFrame = ttk.Frame(root, padding="1 1 2 2")
BoardFrame.grid(column=0, row=2 )


BoardNum1 = ttk.Entry(BoardFrame, justify='center', width=10)
BoardNum1.grid(column=0, row=0)


BoardNum2 = ttk.Entry(BoardFrame, justify='center', width=10)
BoardNum2.grid(column=1, row=0)


BoardNum3 = ttk.Entry(BoardFrame, justify='center', width=10)
BoardNum3.grid(column=2, row=0)


BoardNum4 = ttk.Entry(BoardFrame, justify='center', width=10)
BoardNum4.grid(column=3, row=0)


BoardNum5 = ttk.Entry(BoardFrame, justify='center', width=10)
BoardNum5.grid(column=4, row=0)


BoardNum6 = ttk.Entry(BoardFrame, justify='center', width=10)
BoardNum6.grid(column=5, row=0)


BoardNum7 = ttk.Entry(BoardFrame, justify='center', width=10)
BoardNum7.grid(column=6, row=0)


BoardNum8 = ttk.Entry(BoardFrame, justify='center', width=10)
BoardNum8.grid(column=7, row=0)


BoardNum9 = ttk.Entry(BoardFrame, justify='center', width=10)
BoardNum9.grid(column=8, row=0)


BoardNum10 = ttk.Entry(BoardFrame, justify='center', width=10)
BoardNum10.grid(column=9, row=0)


BoardNum11 = ttk.Entry(BoardFrame, justify='center', width=10)
BoardNum11.grid(column=0, row=1)


BoardNum12 = ttk.Entry(BoardFrame, justify='center', width=10)
BoardNum12.grid(column=1, row=1)


BoardNum13 = ttk.Entry(BoardFrame, justify='center', width=10)
BoardNum13.grid(column=2, row=1)


BoardNum14 = ttk.Entry(BoardFrame, justify='center', width=10)
BoardNum14.grid(column=3, row=1)


BoardNum15 = ttk.Entry(BoardFrame, justify='center', width=10)
BoardNum15.grid(column=4, row=1)


BoardNum16 = ttk.Entry(BoardFrame, justify='center', width=10)
BoardNum16.grid(column=5, row=1)


BoardNum17 = ttk.Entry(BoardFrame, justify='center', width=10)
BoardNum17.grid(column=6, row=1)


BoardNum18 = ttk.Entry(BoardFrame, justify='center', width=10)
BoardNum18.grid(column=7, row=1)


BoardNum19 = ttk.Entry(BoardFrame, justify='center', width=10)
BoardNum19.grid(column=8, row=1)


BoardNum20 = ttk.Entry(BoardFrame, justify='center', width=10)
BoardNum20.grid(column=9, row=1)


BoardNum21 = ttk.Entry(BoardFrame, justify='center', width=10)
BoardNum21.grid(column=0, row=2)


BoardNum22 = ttk.Entry(BoardFrame, justify='center', width=10)
BoardNum22.grid(column=1, row=2)


BoardNum23 = ttk.Entry(BoardFrame, justify='center', width=10)
BoardNum23.grid(column=2, row=2)


BoardNum24 = ttk.Entry(BoardFrame, justify='center', width=10)
BoardNum24.grid(column=3, row=2)


BoardNum25 = ttk.Entry(BoardFrame, justify='center', width=10)
BoardNum25.grid(column=4, row=2)


BoardNum26 = ttk.Entry(BoardFrame, justify='center', width=10)
BoardNum26.grid(column=5, row=2)


BoardNum27 = ttk.Entry(BoardFrame, justify='center', width=10)
BoardNum27.grid(column=6, row=2)


BoardNum28 = ttk.Entry(BoardFrame, justify='center', width=10)
BoardNum28.grid(column=7, row=2)


BoardNum29 = ttk.Entry(BoardFrame, justify='center', width=10)
BoardNum29.grid(column=8, row=2)


BoardNum30 = ttk.Entry(BoardFrame, justify='center', width=10)
BoardNum30.grid(column=9, row=2)


BoardNum31 = ttk.Entry(BoardFrame, justify='center', width=10)
BoardNum31.grid(column=0, row=3)


BoardNum32 = ttk.Entry(BoardFrame, justify='center', width=10)
BoardNum32.grid(column=1, row=3)


BoardNum33 = ttk.Entry(BoardFrame, justify='center', width=10)
BoardNum33.grid(column=2, row=3)


BoardNum34 = ttk.Entry(BoardFrame, justify='center', width=10)
BoardNum34.grid(column=3, row=3)


BoardNum35 = ttk.Entry(BoardFrame, justify='center', width=10)
BoardNum35.grid(column=4, row=3)


BoardNum36 = ttk.Entry(BoardFrame, justify='center', width=10)
BoardNum36.grid(column=5, row=3)


BoardNum37 = ttk.Entry(BoardFrame, justify='center', width=10)
BoardNum37.grid(column=6, row=3)


BoardNum38 = ttk.Entry(BoardFrame, justify='center', width=10)
BoardNum38.grid(column=7, row=3)


BoardNum39 = ttk.Entry(BoardFrame, justify='center', width=10)
BoardNum39.grid(column=8, row=3)


BoardNum40 = ttk.Entry(BoardFrame, justify='center', width=10)
BoardNum40.grid(column=9, row=3)

OptionsFrame = ttk.Frame(root, padding="1 1 2 2")
OptionsFrame.grid(column=0, row=3)

operLable = tk.Label(OptionsFrame, text="Available Operators, Uncheck to restrict")
operLable.grid(column=0, row=0, columnspan=4)

addVal = tk.StringVar()
addDeny = tk.Checkbutton(OptionsFrame, text="add", onvalue="+", offvalue='', variable=addVal)
addDeny.grid(column=0, row=1)
addDeny.select()

subVal = tk.StringVar()
subDeny = tk.Checkbutton(OptionsFrame, text="subtract", onvalue="-", offvalue='', variable=subVal)
subDeny.grid(column=1, row=1)
subDeny.select()

multVal = tk.StringVar()
multDeny = tk.Checkbutton(OptionsFrame, text="multiply", onvalue="*", offvalue='', variable=multVal)
multDeny.grid(column=2, row=1)
multDeny.select()

divVal = tk.StringVar()
divDeny = tk.Checkbutton(OptionsFrame, text="divide", onvalue="/", offvalue='', variable=divVal)
divDeny.grid(column=3, row=1)
divDeny.select()

QueueFrame = ttk.Frame(root, padding="1 1 2 2")
QueueFrame.grid(column=0, row=4)

qCountLbl = tk.Label(QueueFrame, text="Boards In Queue")
qCountLbl.grid(column=0,row=0)

qCountNum = tk.Label(QueueFrame, textvariable=qCount)
qCountNum.grid(column=1, row=0)

btnAddToQ = tk.Button(QueueFrame, text="Add to Queue", command=AddToQueue)
btnAddToQ.grid(column=0, row=1)

btnStartQ = tk.Button(QueueFrame, text="Start Queue", command=StartQueue)
btnStartQ.grid(column=1, row=1)

btnClearBoard = tk.Button(QueueFrame, text="Clear Board", command=ClearBoard)
btnClearBoard.grid(column=2, row=1)



ExpFrame = ttk.Frame(root, padding="1 1 2 2")
ExpFrame.grid(column=2, row=4)
  
BoardLabel = tk.Label(root, text="Enter Board Values below. Leave unneeded spaces blank")
BoardLabel.grid(column=0, row=1)

incExp = tk.BooleanVar()
incExp.set(True)

incExpChk = tk.Checkbutton(ExpFrame, text="Use Exp?", onvalue=True, offvalue=False, variable=incExp)
incExpChk.grid(column=0, row=0)


def ClearScreen():
        for child in BoardFrame.children.values():
                leng = len(child.get())
                child.delete(0, leng + 1)
        BoardNum1.focus_set()
        

def getFileName():
    import tkFileDialog as tkfd
    filename = tkfd.asksaveasfilename()
    return filename

def compileBoard():
    board = []
    state = True
    for child in BoardFrame.children.values():
        val = child.get()
        if val == '':
            continue
        elif val.isdigit():
            board.append(int(val))
        elif val.isdigit() == False:
            state = False
            child.delete(0, len(val)+1)

    if state == False:
        tkm.showinfo("Alert", "Please enter only numbers in the board")
        return 'BoardFail'
    return board

def compileNumVals():
    minVal = minField.get()
    maxVal = maxField.get()
    expVal = expField.get()
    minReq = minNum.get()
    numQuantVal = numQuant.get()
    if not minVal.isdigit() or not maxVal.isdigit() or not expVal.isdigit() or not minReq.isdigit():
        tkm.showinfo("Alert", 'Please only enter numerical Values')
        return
    if int(minVal) >= int(maxVal):
        tkm.showinfo("Alert", 'Min Num must be smaller than max num')
        print "MinVal: ",minVal, "MaxVal: ",maxVal
        return
        
    return int(minVal), int(maxVal), int(expVal), int(minReq), int(numQuantVal)
    
def getOperators(opVars):
        result = []
        for var in  opVars:
                if var.get() != '':
                        result.append(var.get())
        return result

BoardNum1.focus_set()
root.mainloop()





    
