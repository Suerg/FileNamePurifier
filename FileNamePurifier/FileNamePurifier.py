from Parser import Parser      
from LexicalAnalyzer import LexicalAnalyzer

class FileNamePurifier:
    
    def __init__(self, stringAppendToFront, stringAppendToEnd, removeFirstInstanceOfStringsInList, removeAllInstancesOfStringsInList,
                  substringsToPreserve, oldSeperators, seperatorToUse, breakUpByBraces, 
                 breakUpByParens, 
                 breakUpByBrackets, breakUpByCamelCase):
        
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
        
    def CreateParserWithString(self, stringToParse):
        parser = Parser(self.stringAppendToFront, self.stringAppendToEnd, 
                        self.removeFirstInstanceOfStringsInList, 
                        self.removeAllInstancesOfStringsInList,
                  self.substringsToPreserve, self.oldSeperators, self.seperatorToUse, self.breakUpByBraces, 
                 self.breakUpByParens, 
                 self.breakUpByBrackets, self.breakUpByCamelCase, stringToParse);
                 
        return parser;
    
    def PurifyString(self, stringToPurify):
        return self.CreateParserWithString(stringToPurify).outputString