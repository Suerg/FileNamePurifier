import os
from os.path import basename

from FileNamePurifier import FileNamePurifier

class FileSelectorAndPurifier:
    
    def __init__(self, recursive, affectDirectoryNames, startPath, fileNamePurifier):
        self.recursive = recursive
        self.affectDirectoryNames = affectDirectoryNames
        self.startPath = startPath.rstrip('\r\n')
        self.fileNamePurifier = fileNamePurifier
    
        
    
    def PurifyFileNames(self):
        
        if(os.path.isfile(os.path.join(self.startPath))):
            path, name = os.path.split(self.startPath)
            
            self.PurifyFileName(path, name)
            
        else:
            if(self.affectDirectoryNames):
                path, name = os.path.split(self.startPath)
                
                purifiedName = self.fileNamePurifier.PurifyString(name)
                        
                FileSelectorAndPurifier.RenameFileOrDirectory(path, name, purifiedName)
                
                self.startPath = os.path.join(path, purifiedName)
                
            if(self.recursive):
                self.PurifyRecurisve(self.startPath)
            else:
                self.PurifySingleDirectory(self.startPath)
            
    def PurifyFileName(self, path, name):
        name = basename(name)
        
        extension = os.path.splitext(name)[1]
        
        purifiedName = self.fileNamePurifier.PurifyString(os.path.splitext(name)[0])
    
        FileSelectorAndPurifier.RenameFileOrDirectory(path, name, purifiedName + extension)
        
        
    
    def PurifyRecurisve(self, startPath):
        for item in os.listdir(startPath):
            if(os.path.isfile(os.path.join(startPath, item))):
                self.PurifyFileName(startPath, item)
               
            elif(os.path.isdir(os.path.join(startPath, item)) and self.affectDirectoryNames):
                
                if(os.path.isfile(os.path.join(startPath, item)) or self.affectDirectoryNames):
                    purifiedName = self.fileNamePurifier.PurifyString(item)
                    
                    FileSelectorAndPurifier.RenameFileOrDirectory(startPath, item, purifiedName)
    
                    if(os.path.isdir(os.path.join(startPath, purifiedName))):
                        self.PurifyRecurisve(os.path.join(startPath, purifiedName))
                
                elif(os.path.isdir(os.path.join(startPath, item))):
                    self.PurifyRecurisve(os.path.isdir(os.path.join(startPath, item)))
                
    
    @staticmethod
    def RenameFileOrDirectory(pathToDir, oldName, newName):
        if(oldName != newName and len(newName) > 0):
            #TODO: add message about locked files
            try:
                os.rename(os.path.join(pathToDir, oldName), os.path.join(pathToDir, newName))
            except:
                pass
    
    def PurifySingleDirectory(self, pathToDir):
        for item in os.listdir(pathToDir):
            
            if(os.path.isfile(os.path.join(pathToDir, item))):
                self.PurifyFileName(pathToDir, item)
               
            elif(os.path.isdir(os.path.join(pathToDir, item)) and self.affectDirectoryNames):
                
                if(os.path.isfile(os.path.join(pathToDir, item)) or self.affectDirectoryNames):
                    purifiedName = self.fileNamePurifier.PurifyString(item)
                    
                    FileSelectorAndPurifier.RenameFileOrDirectory(pathToDir, item, purifiedName)
            
            
        