import unittest

from FileNamePurifier import FileNamePurifier

class Test(unittest.TestCase):


    def setUp(self):
        self.testPurifier = FileNamePurifier("", "", 
                    [""], [],
                  [], [" ", "_"], " ", 
                  False, True, 
                  True, False,
                  False, False)
        
        self.testPurifier1 = FileNamePurifier("", "", 
                    [""], [],
                  [], [" ", "_"], " ", 
                  False, True, 
                  True, False,
                  True, False)
        
        self.testPurifier2 = FileNamePurifier("", "", 
                    [""], [],
                  [], [" ", "_"], " ", 
                  False, True, 
                  True, False,
                  False, True)

    def tearDown(self):
        pass


    def testPurifyString(self):
        self.assertEqual(
            self.testPurifier.PurifyString("[Kira-Fansub]Bokurano_01v2_(DVD_x264_848x480_24fps_AAC) [82739B97]"),
            "Bokurano 01v2 (848x480)", "Purify Test 1 Failed")
        
        self.assertEqual(
            self.testPurifier.PurifyString("Bokurano 01v2 (848x480)"),
            "Bokurano 01v2 (848x480)", "Purify Test 2 Failed")
        
        self.assertEqual(
            self.testPurifier.PurifyString("[hello]anime .hack"),
            "anime .hack", "Purify Test 3 Failed")
        
        self.assertEqual(
            self.testPurifier1.PurifyString("Bokurano 01v2 (848x480)"),
             "b okurano 01v2 (848x480)", "Purify1 Test 1 Failed")
        
        self.assertEqual(
            self.testPurifier2.PurifyString("[Kira-Fansub]Bokurano_01v2_(DVD_x264_848x480_24fps_AAC) [82739B97]"),
            "BokuranO01v2(848x480)", "Purify2 Test 1 Failed")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()