from LexicalAnalyzer import LexicalAnalyzer

import unittest

class Test(unittest.TestCase):


    def setUp(self):
        self.testLexer1 = LexicalAnalyzer("[otakuFanSubs] animeName [1280x720][218C38]", ["[", "(", "{"], ["]", ")", "}"], [" "], False)
        self.testLexer2 = LexicalAnalyzer("[otakuFanSubs] animeName [1280x720][218C38]", ["[", "(", "{"], ["]", ")", "}"], [" "], True)
        
    def testAddAllElementsInAllListsToSet(self):
        self.assertEqual(self.testLexer1.addAllElementsInAllListsToSet(["[", "(", "{"], {}), {"[", "(", "{"}, "Lexer 1 Failed")
        self.assertEqual(self.testLexer2.addAllElementsInAllListsToSet(["[", "(", "{", "]", ")", "}", " "], {}), {"[", "(", "{", "]", ")", "}", " "}, "Lexer 2 Failed")
    
    def testBuildReservedCharacters(self):
        self.assertEqual(self.testLexer1.buildReservedCharacters(), {"[", "(", "{", "]", ")", "}", " "}, "Lexer 1 Failed")
        self.assertEqual(self.testLexer2.buildReservedCharacters(), {"[", "(", "{", "]", ")", "}", " "}, "Lexer 2 Failed")

    def testIsCharALexeme(self):
        #camelCase test
        for letter in range(ord("A"), ord("Z")):
            self.assertEqual(self.testLexer1.isCharALexeme(chr(letter), {"[", "(", "{"}), False, "Lexer 1 Failed")
            self.assertEqual(self.testLexer2.isCharALexeme(chr(letter), {"[", "(", "{"}), True, "Lexer 2 Failed")

        #lowercase test
        for letter in range(ord("a"), ord("z")):
            self.assertEqual(self.testLexer1.isCharALexeme(chr(letter), {"[", "(", "{"}), False, "Lexer 1 Failed")
            self.assertEqual(self.testLexer2.isCharALexeme(chr(letter), {"[", "(", "{"}), False, "Lexer 2 Failed")
        
        #reserved characters test
        for char in {"[", "(", "{", "]", ")", "}", " "}:
            self.assertEqual(self.testLexer1.isCharALexeme(char, ["[", "(", "{", "]", ")", "}", " "]), True, "Lexer 1 Failed")
            self.assertEqual(self.testLexer2.isCharALexeme(char, ["[", "(", "{", "]", ")", "}", " "]), True, "Lexer 2 Failed")    
        
    def testConvertLexemeToType(self):
        
        #literal_block tests:
        
        #lowercase test
        for letter in range(ord("a"), ord("z")):
            self.assertEqual(self.testLexer1.convertLexemeToType(chr(letter)), self.testLexer1.LITERAL_BLOCK, "Lexer 1 Failed")
            self.assertEqual(self.testLexer2.convertLexemeToType(chr(letter)), self.testLexer2.LITERAL_BLOCK, "Lexer 2 Failed")
        
        #string test
        self.assertEqual(self.testLexer1.convertLexemeToType("I am a literal block!"), self.testLexer1.LITERAL_BLOCK, "Lexer 1 Failed")
        self.assertEqual(self.testLexer2.convertLexemeToType("The quick brown fox jumps over the lazy dog."), self.testLexer2.LITERAL_BLOCK, "Lexer 2 Failed")
        
        #upperCase test
        for letter in range(ord("A"), ord("Z")):
            self.assertEqual(self.testLexer1.convertLexemeToType(chr(letter)), self.testLexer1.LITERAL_BLOCK, "Lexer 1 Failed")
            self.assertEqual(self.testLexer2.convertLexemeToType(chr(letter)), self.testLexer2.BEGIN_BLOCK, "Lexer 2 Failed")

        
        #begin_block test
        for char in ["[", "(", "{"]:
            self.assertEqual(self.testLexer1.convertLexemeToType(char), self.testLexer1.BEGIN_BLOCK, "Lexer 1 Failed")
            self.assertEqual(self.testLexer2.convertLexemeToType(char), self.testLexer2.BEGIN_BLOCK, "Lexer 2 Failed")
            
        #end_block test
        for char in ["]", ")", "}"]:
            self.assertEqual(self.testLexer1.convertLexemeToType(char), self.testLexer1.END_BLOCK, "Lexer 1 Failed")
            self.assertEqual(self.testLexer2.convertLexemeToType(char), self.testLexer2.END_BLOCK, "Lexer 2 Failed")
        
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()