# WinPkgIn Installer for Windows

WinPkgIn let's Windows users to download packages to their devices and it automatically add the package path to the windows Environment variable, System "path". 
Current version = "1.0"

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install WinPkgIn.
```bash
pip install WinPkgIn
```

## Usage
Supporterd extensisions resource with: (.zip/.7z/.rar/.rar5/folders wihout extenstions)etc.
```bash
$ WinPkgIn 
```
### Install Java/Java Script Packages/ Any GitHub Package (.zip files)
#### Java/Maven/Gridle/Node JS/Vue JS etc
`-i <Resource Web URL> <Folder Name>`
```bash
$ WinPkgIn -j python
```
### Install Packages/Folders
#### PHP
`-j <Resource Web URL> <Folder Name>`
```bash
$ WinPkgIn -j python
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
