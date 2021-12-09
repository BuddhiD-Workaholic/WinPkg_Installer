import os
import urllib.request
import subprocess
import ctypes, sys
import getopt
import time
import ssl
from sys import platform
from zipfile import ZipFile

def main():
	#CMD Argumants 
	argumentList = sys.argv[1:]
	options = "hij:"
	long_options = ["Help","Install","J_Packages"]

	PkgName=""
	file_URL=""	
	xy=False

	ssl._create_default_https_context = ssl._create_unverified_context
	
	if len(sys.argv) <= 1:
		print ("  -- No argumants passed! --\n  -i <Web Resource Url> <Folder Name> \n Enter the URL of the resource (eg:.zip/.7z/.rar/<folder>)etc. And then enter a Folder name (eg:PHP/Anyother packages)etc. \n -j <Java Web Resource Url> <Folder Name> \n Enter the URL of the java/GitHub/ resource (eg:.zip/.7z/.rar/<folder>)etc. And then enter a Folder name (eg:Java/MAVEN/Gradle/Any Github sourc files)etc. \n -h for Help \n");
		sys.exit()
		
	try:
		arguments, values = getopt.getopt(argumentList, options, long_options)
		
		for currentArgument, currentValue in arguments:
			if currentArgument in ("-h", "--Help"):
				print ("Git Respository link: https://bit.ly/3EF9TeA \n  -i <Web Resource Url> <Folder Name> \n Enter the URL of the resource (eg:.zip/.7z/.rar/<folder>)etc. And then enter a Folder name (eg:PHP/Anyother packages)etc. \n -j <Java Web Resource Url> <Folder Name> \n Enter the URL of the java/GitHub/ resource (eg:.zip/.7z/.rar/<folder>)etc. And then enter a Folder name (eg:Java/MAVEN/Gradle/Any Github sourc files)etc. \n -h for Help \n");  sys.exit() 
			elif currentArgument in ("-i","--Install") or currentArgument in ("-j","--J_Packages"):
				xy=True
			else: 
				print ("Git Respository link: https://bit.ly/3EF9TeA \n  -i <Web Resource Url> <Folder Name> \n Enter the URL of the resource (eg:.zip/.7z/.rar/<folder>)etc. And then enter a Folder name (eg:PHP/Anyother packages)etc. \n -j <Java Web Resource Url> <Folder Name> \n Enter the URL of the java/GitHub/Anyother resource (eg:.zip/.7z/.rar/<folder>)etc. And then enter a Folder name (eg:Java/Maven/Gridle/Node JS/Vue JS/Any Github sourc files)etc. \n -h for Help \n");  sys.exit() 

	except (IndexError, getopt.error) as err:
		print (str(err)+" ^1")
		sys.exit()

	try:
		if xy==True:
			file_URL=sys.argv[2]
			PkgName=sys.argv[3]
		else: 
			sys.exit()
	except (IndexError, getopt.error) as err:
		print (str(err)+" ^2")
		sys.exit()


	def is_admin():
		try:
			return ctypes.windll.shell32.IsUserAnAdmin()
		except:
			return False

	def javaInstall_F(path):
		global pathName
		try:
			subfolders = [ f.path for f in os.scandir(path) if f.is_dir() ]
			Temppath=os.path.join(subfolders[0], 'bin')
			if os.listdir(Temppath) == []:
				pathName=subfolders[0]
			else:
				pathName=Temppath   
		except:
			subprocess.Popen(r'explorer /select,"'+path+'"')
			print("There's been an error!, Try to set the folder path in the Enviornmantal variables by your self! \n")
			sys.exit()
	
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

			try:
				url = file_URL
				remotefile = urlopen(url)
				blah = remotefile.info()['Content-Disposition']
				value, params = cgi.parse_header(blah)
				pathName=os.path.join(pathName, params["filename"])
				urlretrieve(url, pathName)
			except:
				print("There's been an error!, The Web resource folder is corrupted or wrong WEB resource URL is added! \n")
				sys.exit()
	
		#System Path change
		Path='setx /M path "%path%;'+pathName+'"'
		os.system(Path) 
		print("The mentioned Package is installed 0n "+pathName)
		time.sleep(5)
	else:
		ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)    

	