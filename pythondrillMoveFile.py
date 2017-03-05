import shutil
import os

dirSrc = "C:\\A\\"
dirDst = "C:\\B\\"

def moveFiles():
    names = os.listdir(dirSrc)
    for name in names:
        print 'Moving this file: ' + name + ' from ' + dirSrc + ' to ' + dirDst
        if name.endswith('.txt'):
            shutil.move(dirSrc  + name, dirDst)

            
moveFiles()


if not os.listdir(dirSrc):
    print "The A directory is empty"

newFiles = os.listdir(dirDst)
for newName in newFiles:
    print 'This file: ' + newName + ' is now in directory: ' +  dirDst
