# WinPkgIn Installer for Windows

WinPkgIn let's Windows users to download packages to their devices and it automatically add the package path to the windows Environment variable, System "path". 
Current version = "1.0"

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install WinPkgIn.
```bash
pip install WinPkgIn
```
or
```bash
python pip install WinPkgIn
```

## Usage
Supporterd extensisions resource with: (.zip/.7z/.rar/.rar5/folders wihout extenstions) etc.
```bash
$ WinPkgIn 
```
### Install Java/Java Script Packages/ Any GitHub Package (.zip and noun .zip files)
#### Java/Maven/Gridle/Node JS/Vue JS etc
`-j <Resource Web URL Link> <Folder Name>`
```bash
$ WinPkgIn -j https://download.oracle.com/java/17/latest/jdk-17_windows-x64_bin.zip Java
```

### Install Packages/Folders
#### PHP
`-i <Resource Web URL Link> <Folder Name>`
```bash
$ WinPkgIn -i https://windows.php.net/downloads/releases/php-8.1.0-Win32-vs16-x64.zip PHP 
```

### Help
`-h`
```bash
$ WinPkgIn -h
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
