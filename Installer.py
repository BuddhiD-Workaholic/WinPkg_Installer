import os
import urllib.request
import subprocess as sp
import ctypes, sys
from sys import platform
from zipfile import ZipFile

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

PkgName="pkg"
file_URL="http://cloud.ine.ru/s/JDbPr6W4QXnXKgo/download"    
pathName=os.path.join('C:\Program Files', PkgName)

if is_admin():
    try:
        fullfilename = os.path.join('C:\Program Files', PkgName+".zip")
        urllib.request.urlretrieve(file_URL, fullfilename)

        #File extraction 
        zf = ZipFile(fullfilename, 'r')
        zf.extractall(pathName)
        zf.close()
    except:
        from urllib.request import urlopen
        from urllib.request import urlretrieve
        import cgi

        url = file_URL
        remotefile = urlopen(url)
        blah = remotefile.info()['Content-Disposition']
        value, params = cgi.parse_header(blah)
        pathName=os.path.join('C:\Program Files', params["filename"])
        urlretrieve(url, pathName)
                        
    #System Path change
    os.system('setx /M path "%path%;'+pathName+'"')            
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)    

 