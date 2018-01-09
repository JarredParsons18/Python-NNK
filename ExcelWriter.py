from openpyxl import Workbook
from openpyxl.worksheet import dimensions

def writeVals(outerDict, innerDict, filename):
    columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', \
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    
    wb = Workbook()
    ws = wb.active


    
    ws.title = 'Number Combinations'

    ws.merge_cells('B1:D1')
    ws['B1'] = 'National Number Knockout Number Combinations'

    ws['A4'] = 'Numbers'
    ws['B4'] = 'Unique Answers Found'
    ws['C4'] = 'Begin Formulas'

    outerDictKeys = sorted(outerDict.keys())
    row = 5
    for key in outerDictKeys:
        ws['A'+str(row)] = str(key)
        ws['B'+str(row)] = len(outerDict[key])
        col = 2
        mod = ''
        modNum = -1
        for ans in outerDict[key]:
            if col > 25:
                col = col - 26
                modNum += 1
                mod = columns[modNum]
                
                
        
            try:
                innerKey = key, ans
                for func in innerDict[innerKey]:
                    if mod != '':
                        ws[mod+columns[col]+str(row)] = func
                        col += 1
                    else:
                        ws[columns[col]+str(row)] = func
                        col += 1
                    
            except:
                continue
        row += 1

    try:
        wb.save(filename+'.xlsx')
        return True
    except:
        return 'Fail'
		
		
def writeTextFile(outerDict, filename){

	numFile = fopen()
}
    
    
        
        
    

