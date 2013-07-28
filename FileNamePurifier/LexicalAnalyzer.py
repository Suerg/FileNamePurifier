class LexicalAnalyzer:
    BEGIN_BLOCK   = 0
    END_BLOCK     = 1
    LITERAL_BLOCK = 2  

    def __init__(self, stringToAnalyze, beginBlockList, endBlockList, seperatorList, camelCaseAsDelimiter):
        
        self.beginBlockList       = beginBlockList
        self.endBlockList         = endBlockList
        self.seperatorList        = seperatorList
        self.camelCaseAsDelimiter = camelCaseAsDelimiter
        
        tokenListAndLookupTable = self.tokenizeAndBuildLookupTableFromString(stringToAnalyze)
        
        self.tokenList   = tokenListAndLookupTable[0]
        self.lookupTable = tokenListAndLookupTable[1]
    
    def addAllElementsInAllListsToSet(self, listOfListsWithElementsToAdd, setToAddElementsTo):
        newSet = set(setToAddElementsTo)
        for listWithElements in listOfListsWithElementsToAdd:
            for element in listWithElements:
                newSet.add(element)
        return newSet
        
    def buildReservedCharacters(self):
        setReservedCharacters = set()
        
        setReservedCharacters = self.addAllElementsInAllListsToSet(
                                    [self.beginBlockList, self.endBlockList, self.seperatorList], setReservedCharacters)
        
        return setReservedCharacters
    
    def isCharALexeme(self, char, reservedCharacters):
        return (self.camelCaseAsDelimiter and (char >= "A" and char <= "Z")) or (char in reservedCharacters)
    
    def convertLexemeToType(self, lexeme):
        blockType = self.LITERAL_BLOCK
        
        if(lexeme in self.beginBlockList or ( (lexeme >= "A" and lexeme <= "Z") and self.camelCaseAsDelimiter and len(lexeme) == 1)):
            blockType = self.BEGIN_BLOCK
        elif(lexeme in self.endBlockList):
            blockType = self.END_BLOCK
        return blockType
        
    def createToken(self, currentLexeme, lexemeIndex):
        return (self.convertLexemeToType(currentLexeme), lexemeIndex)
    
    def tokenizeAndBuildLookupTableFromString(self, originalString):
        tokens      = list() # list of token tuples: [(intType, intIndex)...]
        lookupTable = list() # list of lexeme strings
        
        currentLexeme = ""
        
        reservedCharacters = self.buildReservedCharacters()
        
        lexemeCount = 0
        
        for char in originalString:
            if(self.isCharALexeme(char, reservedCharacters)) :
                if(len(currentLexeme) > 0):
                    lookupTable.append(currentLexeme)
                    tokens.append(self.createToken(currentLexeme, lexemeCount))
                    lexemeCount += 1
                
                currentLexeme = ""
                currentLexeme += char
                lookupTable.append(currentLexeme)
                
                tokens.append(self.createToken(currentLexeme, lexemeCount))
                lexemeCount += 1
                currentLexeme = ""
            else:
                currentLexeme += char
        
        if(len(currentLexeme) > 0):
            lookupTable.append(currentLexeme)
            tokens.append(self.createToken(currentLexeme, lexemeCount))
            lexemeCount += 1
        
        return (tokens, lookupTable)