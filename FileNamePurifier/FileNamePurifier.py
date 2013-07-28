from Parser import Parser      
from LexicalAnalyzer import LexicalAnalyzer

class FileNamePurifier:
    
    def __init__(self, stringAppendToFront, stringAppendToEnd, removeFirstInstanceOfStringsInList, removeAllInstancesOfStringsInList,
                  substringsToPreserve, oldSeperators, seperatorToUse, breakUpByBraces, 
                 breakUpByParens, 
                 breakUpByBrackets, breakUpByCamelCase, startLocation):
        
        self.stringAppendToFront = stringAppendToFront
        self.stringAppendToEnd   = stringAppendToEnd
        
        self.removeFirstInstanceOfStringsInList = removeFirstInstanceOfStringsInList
        self.removeAllInstancesOfStringsInList  = removeAllInstancesOfStringsInList
        
        self.substringsToPreserve = substringsToPreserve
        
        self.oldSeperators  = oldSeperators
        self.seperatorToUse = seperatorToUse
        
        self.breakUpByBraces    = breakUpByBraces
        self.breakUpByParens    = breakUpByParens
        self.breakUpByBrackets  = breakUpByBrackets
        self.breakUpByCamelCase = breakUpByCamelCase
        
        
lexer = LexicalAnalyzer("[otakuFanSubs] anime [720p]", ["(", "[", "{"], [")", "]", "}"], [" "], True)

#print lexer.lookupTable
#print lexer.tokenList           

parser = Parser("", "", [], [], [], [], "", True, True, True, False, "[otakuFanSubs] animeName [720p][218C38]")                   

print parser.outputString

"""
stringAppendToFront, 
stringAppendToEnd, 
removeFirstInstanceOfStringsInList, 
removeAllInstancesOfStringsInList, 
substringsToPreserve, 
oldSeperators, 
seperatorToUse, 
breakUpByBraces, 
breakUpByParens, 
breakUpByBrackets, 
breakUpByCamelCase, 
originalString):
"""