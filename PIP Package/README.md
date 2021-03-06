# WinPkgIn Installer for Windows

WinPkgIn let's Windows users to download packages to their devices and it automatically add the package path to the windows Environment variable, System "path". 
Current version = "1.0"

#### Supported Windows versions:- Windows 7+ 

[![Image.png](https://i.postimg.cc/XYR6VpQT/Image.png)](https://postimg.cc/w1QG2TKV)

## Installation
#### Method 01: 
Downlaod the WinPkgIn.exe file in [WinPkg_Installer](https://github.com/BuddhiD-Workaholic/WinPkg_Installer/tree/main/Installer%20(.exe)%20file) directory and add the downloaded folder path to to the System path/ Environment variable. 
```bash
WinInstaller
```

#### Method 02: 
Use the package manager [pip](https://pypi.org/project/WinInstaller/) to install WinPkgIn.
```bash
pip install WinInstaller
```
or
```bash
python pip install WinInstaller
```

## Usage
Supporterd extensisions resource with: (.zip/.7z/.rar/.rar5/folders wihout extenstions) etc.
```bash
$ WinInstaller 
```
### Install Java/Java Script Packages/ Any GitHub Package (.zip and noun .zip files)
#### Java/Maven/Gridle/Node JS/Vue JS etc
`-j <Resource Web URL Link> <Folder Name>`
```bash
$ WinInstaller -j https://download.oracle.com/java/17/latest/jdk-17_windows-x64_bin.zip Java
```

### Install Packages/Folders
#### PHP
`-i <Resource Web URL Link> <Folder Name>`
```bash
$ WinInstaller -i https://windows.php.net/downloads/releases/php-8.1.0-Win32-vs16-x64.zip PHP 
```

### Help
`-h`
```bash
$ WinInstaller -h
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
