import shutil
import os
import datetime as dt


dirSrc = "C:\\A\\"
dirDst = "C:\\B\\"

def moveFiles():
    names = os.listdir(dirSrc)
    for name in names:
        now = dt.datetime.now()
        ago = now-dt.timedelta(days=1)

        st = os.stat(dirSrc + name)    
        mtime = dt.datetime.fromtimestamp(st.st_mtime)
        if mtime > ago:
            if name.endswith('.txt'):
                print('%s modified %s'%(name, mtime))
                print 'This file is less than 24 hours old' + name
                shutil.move(dirSrc  + name, dirDst)
            
moveFiles()



newFiles = os.listdir(dirDst)
for newName in newFiles:
    print 'This file: ' + newName + ' was modified in the last 24 hours and is now in directory: ' +  dirDst
