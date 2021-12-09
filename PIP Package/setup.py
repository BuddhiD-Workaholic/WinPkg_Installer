from setuptools import setup, find_packages

long_description = "This package let's windows users to downlaod and install .zip or anyother files including adding the path to the Enviornmental Variables bychanging the PATH variable"

setup(
		name ='WinPkgIn',
		author="Buddhi Dhananjaya",
        author_email="buddhi_dhananjaya@outlook.com",
        description="This package let's windows users to downlaod and install .zip or anyother files including adding the path to the Enviornmental Variables bychanging the PATH variable",
		url ='https://github.com/BuddhiD-Workaholic/WinPkg_Installer.git',
		long_description = long_description,
		long_description_content_type ="text/markdown",
		license ='MIT',
		packages = find_packages(),
		entry_points ={
			'console_scripts': [
				'WinPkgIn = WinPkg.WinPkgIn:main'
			]
		},
		classifiers =(
			"Programming Language :: Python :: 3",
			"License :: OSI Approved :: MIT License",
			"Operating System :: Microsoft :: Windows",
		),
		keywords ='WinPkgIn WindowsPkgIn WindowsPkg Windowspackagemanager package manager python package Windows Installer',
		zip_safe = False
)
