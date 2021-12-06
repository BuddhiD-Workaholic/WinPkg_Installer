import os
import urllib.request
import subprocess as sp
import ctypes, sys
import getopt
import time
from sys import platform
from zipfile import ZipFile

#CMD Argumants 
argumentList = sys.argv[1:]
options = "hij:"
long_options = ["Help", "Install","Java_Packages"]

PkgName=""
file_URL=""	
xy=False

try:
	arguments, values = getopt.getopt(argumentList, options, long_options)

	for currentArgument, currentValue in arguments:
		if currentArgument in ("-h", "--Help"):
			print (" -i <Web Resource Url> <Folder Name> \n Enter the URL of the resource (eg:.zip/.7z/.rar/<folder>)etc. And then enter a Folder name (eg:GIT/PHP)etc. \n -j <Java Web Resource Url> <Folder Name> \n Enter the URL of the java resource (eg:.zip/.7z/.rar/<folder>)etc. And then enter a Folder name (eg:Java/MAVEN/Gradle)etc. \n") 
		elif currentArgument in ("-i","--Install") or currentArgument in ("-j","--Java_Packages"):
		    xy=True

except getopt.error as err:
	print (str(err))

try:
    if xy==True:
        file_URL=sys.argv[2]
        PkgName=sys.argv[3] 
except getopt.error as err:
	print (str(err))


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def javaInstall_F(path):
    global pathName
    subfolders = [ f.path for f in os.scandir(path) if f.is_dir() ]
    pathName=os.path.join(subfolders[0], 'bin')
    print ("Path: "+pathName)

if is_admin():
    pathName=os.path.join('C:\PROGRA~1', PkgName)
    if not os.path.exists(pathName):
        os.makedirs(pathName)
    else:
        print("This device already contain a "+PkgName+" folder on this location "+pathName+"\n Delete that file to proceed with the instalaltion!")
        time.sleep(40)
        sys.exit()
    try:
        Temp=PkgName+".zip"
        fullfilename = os.path.join(pathName, Temp)
        urllib.request.urlretrieve(file_URL, fullfilename)

        #File extraction 
        zf = ZipFile(fullfilename, 'r')
        zf.extractall(pathName)
        zf.close()
        
        if currentArgument in ("-j","--Java_Packages"):
            javaInstall_F(pathName)
        
    except:
        from urllib.request import urlopen
        from urllib.request import urlretrieve
        import cgi

        url = file_URL
        remotefile = urlopen(url)
        blah = remotefile.info()['Content-Disposition']
        value, params = cgi.parse_header(blah)
        pathName=os.path.join(pathName, params["filename"])
        urlretrieve(url, pathName)
    
    #System Path change
    Path='setx /M path "%path%;'+pathName+'"'
    os.system(Path) 
    print("The mentioned Package is installed 0n "+pathName)
    time.sleep(5)
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)    

 