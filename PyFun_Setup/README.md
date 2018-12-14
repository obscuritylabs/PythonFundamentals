# Python Fun(damentals)
## Python 3 Setup


**Alexander Rymdeko-Harvey**
Obscurity Labs
```
* Innovation  
* Expert Training
* Advanced Security Services
```

<img src="https://obscuritylabs.com/wp-content/uploads/2018/04/OL-3d-landscape-positive.jpg" alt="Kitten"
	title="A cute kitten" width="225" height="100" />

<small>Copyright (c) 2018 Alexander Rymdeko-Harvey & Obscurity Labs LLC.</small>

---

# Introduction 

- Who am I? 
- Why this is important?
- Free training?

---

# Install Demo and Instructions 
1) Windows/Mac/Ubuntu Install Instructions
2) Python 3.6+ & Packages 
4) Visual Studio Code
5) Pipenv Instruction

---
### Windows 10
You will need Chocolatey, this can be installed easily with a one-line download:
```cmd
@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
```
NOTE: Install guide can be found here [https://chocolatey.org/docs/installation#installing-chocolatey](https://chocolatey.org/docs/installation#installing-chocolatey)

---
### Windows 10 Cont.
Now we setup our tools:
```powershell
choco install -y python vscode git cmder
python -m pip install -U pip
pip install --user --upgrade pipenv
```
You may need to add pipenv to your path (Ex. here was my path):
```powershell
C:\Users\Killswitch3\AppData\Roaming\Python\Python36\Scripts
```

---
### Windows 10 Cont.
Now our environment is ready to start to get to work within PowerShell:
```powershell
PS C:\Users\Killswitch3\tools> git clone https://github.com/obscuritylabs/PythonFundamentals.git 
PS C:\Users\Killswitch3\tools> cd .\PythonFundamentals\
PS C:\Users\Killswitch3\tools> python -m pipenv install
PS C:\Users\Killswitch3\tools> python -m pipenv shell
```