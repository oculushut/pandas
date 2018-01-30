REM %~dp0 => Current directory
REM requires pip
REM syntax for pip: py -m pip <package to install.
REM e.g. to install aws cli: py -m pip awscli

REM https://docs.aws.amazon.com/cli/latest/userguide/awscli-install-windows.html#awscli-install-windows-pip
REM requires 7-zip commandline - current location hard coded (7zip examples: https://www.poftut.com/7z-command-tutorial-examples-compress-extract-files-linux/)

REM make the package directory
mkdir "%~dp0package"

REM copy the python files
xcopy "%~dp0hello_python.py" "%~dp0package\"

REM place the dependent packages into the package directory
py -m pip install urllib3 -t "%~dp0package"
py -m pip install beautifulsoup4 -t "%~dp0package"
py -m pip install pandas -t "%~dp0package"

REM zip it all up (this is the format that AWS requires
"C:\Program Files\7-Zip\7z" a aws_package.zip "c:\dev\pharmify\1-hello\package\*"
