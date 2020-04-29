---
marp: true
_class: lead
paginate: true
footer: 'Copyright (c) 2020 Obscurity Labs LLC.'
---
# Python Fun(damentals)
## Installing Python Modules 

**Alexander Rymdeko-Harvey**
Obscurity Labs
```text
* Python Package Manager
* Using `pip`
```

![height:90px](https://obscuritylabs.com/wp-content/uploads/2019/11/OL-3d-landscape-positive-transparent.png)

---
# Python Package Manager
Like other major languages has the main choice of a package manager. PyPi provides this support to the open-source community and contributors. It provides you the ability to publish your open source project to the world with a simple command to install. PyPi can be found at https://pypi.org/. Which will provide you the following:

* Single repository to share your distributed package
* Strong version control
* Great CLI support to use packages within your build system
    * `pip` - The Python Package Installer (https://pip.pypa.io/en/stable/installing/)

---
# Installing Python Modules Using `pip`

### Install requests from PyPI
```bash
$ pip install requests
Collecting requests
  Downloading requests-2.23.0-py2.py3-none-any.whl (58 kB)
     |████████████████████████████████| 58 kB 5.8 MB/s 
Collecting urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1
  Downloading urllib3-1.25.9-py2.py3-none-any.whl (126 kB)
     |████████████████████████████████| 126 kB 23.2 MB/s 
Collecting chardet<4,>=3.0.2
  Downloading chardet-3.0.4-py2.py3-none-any.whl (133 kB)
     |████████████████████████████████| 133 kB 77.5 MB/s 
Collecting certifi>=2017.4.17
  Downloading certifi-2020.4.5.1-py2.py3-none-any.whl (157 kB)
     |████████████████████████████████| 157 kB 98.3 MB/s 
Collecting idna<3,>=2.5
  Downloading idna-2.9-py2.py3-none-any.whl (58 kB)
     |████████████████████████████████| 58 kB 76.2 MB/s 
Installing collected packages: urllib3, chardet, certifi, idna, requests
Successfully installed certifi-2020.4.5.1 chardet-3.0.4 idna-2.9 requests-2.23.0 urllib3-1.25.9

```

---
# Installing Python Modules Using `pip` cont.
### Install specific version of requests
```bash
$ pip install requests==2.22.0
Collecting requests==2.22.0
  Downloading requests-2.22.0-py2.py3-none-any.whl (57 kB)                                   
     |████████████████████████████████| 57 kB 3.5 MB/s 
Collecting idna<2.9,>=2.5
  Downloading idna-2.8-py2.py3-none-any.whl (58 kB)
     |████████████████████████████████| 58 kB 14.5 MB/s 
Installing collected packages: idna, requests
  Attempting uninstall: idna
    Found existing installation: idna 2.9
    Uninstalling idna-2.9:
      Successfully uninstalled idna-2.9
  Attempting uninstall: requests
    Found existing installation: requests 2.23.0
    Uninstalling requests-2.23.0:
      Successfully uninstalled requests-2.23.0
Successfully installed idna-2.8 requests-2.22.0
```

---
# Installing Python Modules Using `pip` cont.
### List packages installed
```bash
$ pip freeze 
ansible==2.9.7
asn1crypto==0.24.0
bcrypt==3.1.6
configparser==3.5.0b2
cryptography==2.6.1
future==0.18.2
Glances==3.1.4.1
certifi==2020.4.5.1
chardet==3.0.4
idna==2.8
requests==2.22.0
urllib3==1.25.9
```

---
# Specifying requirements in `requirements.txt` 
* The `requirements.txt` file is used for specifying what python packages are required to run the project. 
* Typically the requirements.txt file is located in the root directory of your project.

You can easily install your packages (Specific Versions Known to Work for the Package) using pip and the `requirements.txt` file:

```bash
$ cat requirements.txt
requests==2.22.0
```

```bash
$ pip install -r requirements.txt
Collecting requests
  Downloading requests-2.23.0-py2.py3-none-any.whl (58 kB)
     |████████████████████████████████| 58 kB 5.8 MB/s 
..::SNIP::..
Successfully installed certifi-2020.4.5.1 chardet-3.0.4 idna-2.9 requests-2.23.0 urllib3-1.25.9
```

---
# Lab_2.py
**Tasking**
Using the new `pip` command perform the following:
1. Open the custom `requirements.txt` file in the `02_python3_tooling_build_systems/` folder
2. Add the python package `pytest` and specify latest `5.4.1`
3. Install these packages using `pip`

**Testing your work**
**NOTE:** you should see Green `PASS` statements indicating you completed the lab
```bash
$ cd 01_python3_tooling_build_systems
$ python lab_1.py
```
