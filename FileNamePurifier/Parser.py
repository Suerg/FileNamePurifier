from LexicalAnalyzer import LexicalAnalyzer
class Parser:
    """
    TODO:
        add camelCase separator logic
    """
    BEGIN_BLOCK   = 0
    END_BLOCK     = 1
    LITERAL_BLOCK = 2  
        
        
    def __init__(self, stringAppendToFront, stringAppendToEnd, removeFirstInstanceOfStringsInList, removeAllInstancesOfStringsInList,
                  substringsToPreserve, oldSeperators, seperatorToUse, breakUpByBraces, 
                 breakUpByParens, 
                 breakUpByBrackets, breakUpByCamelCase, originalString):
        
        #self.substringsToPreserve = substringsToPreserve       #may not make instance variable
        self.oldSeperators        = oldSeperators
        self.seperatorToUse       = seperatorToUse
        
        self.breakUpByBraces    = breakUpByBraces
        self.breakUpByParens    = breakUpByParens
        self.breakUpByBrackets  = breakUpByBrackets
        self.breakUpByCamelCase = breakUpByCamelCase
    
        self.originalString = originalString
        self.lexer = LexicalAnalyzer(originalString, self.createBeginBlocks(), self.createEndBlocks(), [" "], self.breakUpByCamelCase)
        
        self.outputString     =  self.lexemeListToString(self.constructString())
        
        
        preservedList = self.stringToListPreserveStringsInList(self.outputString, substringsToPreserve)
        replacedList  = self.replaceInstancesOfElementInListWithItem(preservedList, oldSeperators, 
                                                                 seperatorToUse, substringsToPreserve)
        self.outputString = self.lexemeListToString(replacedList).strip()
        
        for substring in removeAllInstancesOfStringsInList:
            self.outputString = self.replaceInstancesOfStringInStringWithString(substring, "", self.outputString)
        
        for substring in removeFirstInstanceOfStringsInList:
            self.outputString = self.removeFirstInstanceOfStringFromString(substring, self.outputString)
        
        self.outputString = stringAppendToFront + self.outputString
        
        self.outputString += stringAppendToEnd
        
    
    def replaceInstancesOfElementsInListInStringWithItem(self, listToReplace, replaceWith, inputString):
        currentString = inputString
        
        for item in listToReplace:
            if(len(item) > 1 or len(replaceWith) > 1):
                currentString = self.replaceInstancesOfStringInStringWithString(item, replaceWith, currentString)
            else:
                currentString = self.replaceInstancesOfCharsInStringWithChar([item], replaceWith, inputString)
                 
        return currentString
    
    def removeFirstInstanceOfStringFromString(self, stringToRemove, inputString):
        seperatedString = self.stringToListPreserveStringsInList(inputString, [stringToRemove])
        
        listStringsAfterReplace = list(seperatedString)
        
        for stringIndex in range(len(seperatedString)):
            if(seperatedString[stringIndex] == stringToRemove):
                listStringsAfterReplace[stringIndex] = ""
                break
        
        return self.lexemeListToString(listStringsAfterReplace)
        
        
    def replaceInstancesOfStringInStringWithString(self, stringToReplace, replaceWith, inputString):
        seperatedString = self.stringToListPreserveStringsInList(inputString, [stringToReplace])
        
        listStringsAfterReplace = list(seperatedString)
        
        for stringIndex in range(len(seperatedString)):
            if(seperatedString[stringIndex] == stringToReplace):
                listStringsAfterReplace[stringIndex] = replaceWith
        
        return self.lexemeListToString(listStringsAfterReplace)
        
    def replaceInstancesOfCharsInStringWithChar(self, listToReplace, replaceWith, inputString):
        replacedString = ""
        
        for char in inputString:
            charToAppend = char
            if(char in listToReplace):
                charToAppend = replaceWith
            replacedString += charToAppend
        
        return replacedString 
       
    def replaceInstancesOfElementInListWithItem(self, stringsToCheck, toReplace, replaceWith, stringsToPreserve):
        newList = list(stringsToCheck)
        for stringIndex in range(len(stringsToCheck)):
            if((stringsToCheck[stringIndex] in stringsToPreserve) == False):
                newList[stringIndex] = self.replaceInstancesOfElementsInListInStringWithItem(toReplace, 
                                                                                         replaceWith, 
                                                                                         stringsToCheck[stringIndex])
        return newList
            
    def stringStartsWith(self, partialString, fullString):
        result = True
        if(len(partialString) == 0):
            result = False
            
        for charIndex in range(len(partialString)):
            if(charIndex < len(fullString)):
                if(partialString[charIndex] != fullString[charIndex]):
                    result = False
            else:
                result = False
        
        return result
    
    def anyStringInListStartsWith(self, partialString, listToCheck):
        result = False
        
        for string in listToCheck:
            if(self.stringStartsWith(partialString, string)):
                result = True
        
        return result
    
    def stringToListPreserveStringsInList(self, inputString, stringsToPreserve):
        outputList = list()
        
        currentString = ""
        previousResultOfMatch = False
        for char in inputString:
            
            if(self.anyStringInListStartsWith(char, stringsToPreserve) != previousResultOfMatch):
                if(self.anyStringInListStartsWith(currentString, stringsToPreserve)):
                    if(currentString in stringsToPreserve):
                        outputList.append(currentString)
                        currentString = ""
                else:
                    if(len(currentString) > 0):
                        outputList.append(currentString)
                        currentString = ""
            
            currentString += char
            
                    
            previousResultOfMatch = self.anyStringInListStartsWith(currentString, stringsToPreserve)
        
        outputList.append(currentString)
            
        return outputList
                 
    def createBeginBlocks(self):
        beginBlocks = list()
        if(self.breakUpByBrackets):
            beginBlocks.append("[")
        if(self.breakUpByParens):
            beginBlocks.append("(")
        if(self.breakUpByBraces):
            beginBlocks.append("{")
        return beginBlocks
        
    def createEndBlocks(self):
        endBlocks = list()
        if(self.breakUpByBrackets):
            endBlocks.append("]")
        if(self.breakUpByParens):
            endBlocks.append(")")
        if(self.breakUpByBraces):
            endBlocks.append("}")
        return endBlocks
    
    
    def findIndexOfFirstInstance(self, startingIndex, blockType, seperator):
        indexOfResult = -1 # -1 indicates no instance found
        
        for i in range(startingIndex, len(self.lexer.tokenList)):
            if(self.lexer.tokenList[i][0] == blockType):
                if(self.lexer.lookupTable[i] == seperator):
                    indexOfResult = i
                    break
                
        return indexOfResult
    
    def findIndexOfFirstEndBlock(self, startIndex, seperatorType):
        blockType = self.END_BLOCK
        return self.findIndexOfFirstInstance(startIndex, blockType, seperatorType)
    
    def findIndexOfFirstBraceEndBlock(self, startIndex, lookupTable, tokens):
        return self.findIndexOfFirstEndBlock(startIndex, "}")
    
    def findIndexOfFirstParenEndBlock(self, startIndex):
        return self.findIndexOfFirstEndBlock(startIndex, ")")
    
    def findIndexOfFirstBracketEndBlock(self, startIndex):
        return self.findIndexOfFirstEndBlock(startIndex, "]")
    
    def findIndexLexemeEndBlock(self, lexemeIndex):
        lexemeAtIndex   = self.lexer.lookupTable[lexemeIndex]
        indexOfEndBlock = -1 # -1 indicates no end block found
        
        if(self.breakUpByBraces and lexemeAtIndex == "{"):
            indexOfEndBlock = self.findIndexOfFirstBraceEndBlock(lexemeIndex)
        if(self.breakUpByParens and lexemeAtIndex == "("):
            indexOfEndBlock = self.findIndexOfFirstParenEndBlock(lexemeIndex)
        if(self.breakUpByBrackets and lexemeAtIndex == "["):
            indexOfEndBlock = self.findIndexOfFirstBracketEndBlock(lexemeIndex)
        
        return indexOfEndBlock
        
    def buildLexemeList(self, startIndex, inclusiveEndIndex):
        lexemList = list()
        
        for i in range(startIndex, inclusiveEndIndex + 1):
            lexemList.append(self.lexer.lookupTable[i])
        return lexemList
    
    def createResolutionSet(self):
        resolutionSet = set()
        
        resolutionSet.add("480p")
        resolutionSet.add("720p")
        resolutionSet.add("1080p")
        resolutionSet.add("640x480")
        resolutionSet.add("800x480")
        resolutionSet.add("848x480")
        resolutionSet.add("720x480")
        resolutionSet.add("854x480")
        resolutionSet.add("1280x720")
        resolutionSet.add("1024x768")
        resolutionSet.add("1366x768")
        resolutionSet.add("1920x1080")
        
        resolutionSet.add("640 x 480")
        resolutionSet.add("800 x 480")
        resolutionSet.add("720 x 480")
        resolutionSet.add("854 x 480")
        resolutionSet.add("1280 x 720")
        resolutionSet.add("1024 x 768")
        resolutionSet.add("1366 x 768")
        resolutionSet.add("1920 x 1080")
        
        resolutionSet.add("640x480")
        resolutionSet.add("800x480")
        resolutionSet.add("720x480")
        resolutionSet.add("854x480")
        resolutionSet.add("1280x720")
        resolutionSet.add("1024x768")
        resolutionSet.add("1366x768")
        resolutionSet.add("1920x1080")
        
        return resolutionSet
    
    def keepLexemeList(self, lexemeListToCheck):
        return (len(self.findResoultionInLexemeList(lexemeListToCheck)) > 0)
    
    def lexemeListToString(self, lexemeList):
        return "".join(lexemeList)
        
    def findResoultionInLexemeList(self, lexemeList):
        resolutionSet = self.createResolutionSet()
        
        resolutionString = ""
        
        stringFormOfLexeme = self.lexemeListToString(lexemeList)
        
        for resolution in resolutionSet:
            if(resolution in stringFormOfLexeme):
                resolutionString = resolution
        
        return resolutionString
    
    def findStartingType(self, lexemeList):
        
        BLOCK_BRACES   = 0
        BLOCK_BRACKETS = 1
        BLOCK_PARENS   = 2
        
        blockType = 3
        
        for lexeme in lexemeList:
            if(blockType == 3):
                if(self.breakUpByBraces):
                    if(lexeme == "{"):
                        blockType           = BLOCK_BRACES
                if(self.breakUpByBrackets):
                    if(lexeme == "["):
                        blockType           = BLOCK_BRACKETS
                if(self.breakUpByParens):
                    if(lexeme == "("):
                        blockType           = BLOCK_PARENS  
        return blockType  
    
    def purifyLexemeList(self, lexemeListToPurify):         
        blockType = 3 #indicates no block found
        
        BLOCK_BRACES   = 0
        BLOCK_BRACKETS = 1
        BLOCK_PARENS   = 2
                
        blockTypeList = [self.breakUpByBraces, self.breakUpByBrackets, self.breakUpByParens, False]
            
        resolutionString = self.findResoultionInLexemeList(lexemeListToPurify)
        
        blockType = self.findStartingType(lexemeListToPurify)
        
        blockStart = ""
        blockEnd   = ""
        
        if(blockTypeList[blockType]):
            if(blockType == BLOCK_BRACES):
                blockStart = "{"
                blockEnd   = "}"
            elif(blockType == BLOCK_BRACKETS):
                blockStart = "["
                blockEnd   = "]"
            elif(blockType == BLOCK_PARENS):
                blockStart = "("
                blockEnd   = ")"
        
        return blockStart + resolutionString + blockEnd
    
    def firstInstanceOfBeginBlock(self, startIndex):
        smallestIndex = self.findIndexOfFirstInstance(startIndex, self.BEGIN_BLOCK, "{")
        
        braceFirstBegin = self.findIndexOfFirstInstance(startIndex, self.BEGIN_BLOCK, "[")
        if(braceFirstBegin < smallestIndex):
            smallestIndex = braceFirstBegin
         
        parenFirstBegin = self.findIndexOfFirstInstance(startIndex, self.BEGIN_BLOCK, "(")
        if(parenFirstBegin < smallestIndex):
            smallestIndex = parenFirstBegin
            
        return smallestIndex
    
    def firstInstanceOfEndBlock(self, startIndex):
        smallestIndex = self.findIndexOfFirstInstance(startIndex, self.END_BLOCK, "}")
        
        braceFirstEnd = self.findIndexOfFirstInstance(startIndex, self.END_BLOCK, "]")
        if(braceFirstEnd < smallestIndex):
            smallestIndex = braceFirstEnd
         
        parenFirstEnd = self.findIndexOfFirstInstance(startIndex, self.END_BLOCK, ")")
        if(parenFirstEnd < smallestIndex):
            smallestIndex = parenFirstEnd
            
        return smallestIndex
        
        
    def firstInstanceOfBeginOrEndBlock(self, startIndex):
        smallestIndex = self.firstInstanceOfBeginBlock(startIndex)
        
        firstEndBlock = self.firstInstanceOfEndBlock(startIndex)
        if(firstEndBlock < smallestIndex):
            smallestIndex = firstEndBlock
        
        return smallestIndex
        
    def constructString(self):
        outputStrings = list()
        
        currentString = ""
        
        for currentTokenNumber in range(len(self.lexer.tokenList)):
            if(self.lexer.tokenList[currentTokenNumber][0] == self.BEGIN_BLOCK):
                outputStrings.append(currentString)
                
                indexOfLexeme   = self.lexer.tokenList[currentTokenNumber][1]
                indexOfEndBlock = self.findIndexLexemeEndBlock(indexOfLexeme)
                
                if(indexOfEndBlock != -1):
                    block = self.buildLexemeList(indexOfLexeme, indexOfEndBlock)
                    if(self.keepLexemeList(block)):
                        purifiedLexemeList = self.purifyLexemeList(block);
                        outputStrings.append(purifiedLexemeList)
                    
                    currentTokenNumber = indexOfEndBlock
                    
            elif(self.lexer.tokenList[currentTokenNumber][0] == self.END_BLOCK):
                currentString = ""
                
            else:
                currentString += self.lexer.lookupTable[self.lexer.tokenList[currentTokenNumber][1]]
                
        return outputStrings
