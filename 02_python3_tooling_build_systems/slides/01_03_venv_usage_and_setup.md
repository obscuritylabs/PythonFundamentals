---
marp: true
_class: lead
paginate: true
footer: 'Copyright (c) 2020 Obscurity Labs LLC.'
---

# Python Fun(damentals)
## Venv Usage & Setup

**Alexander Rymdeko-Harvey**
Obscurity Labs
```text
* Directory Structure
* Config Files
+
```

![height:90px](https://obscuritylabs.com/wp-content/uploads/2019/11/OL-3d-landscape-positive-transparent.png)

---
# Python `venv` Module

The venv module provides support for creating lightweight “virtual environments” with their own site directories, optionally isolated from system site directories.

* Each virtual environment has its own Python binary.
    * which matches the version of the binary that was used to create this environment.
* Can have its own independent set of installed Python packages in its site directories.
* Prevents you from destroying your local development environment.
* Buys you the ability to test, run and build code in a controlled way.
* Comes built-in with Python3
* Very low level and root of many build system tools (pipenv, Poetry, etc.)

---
# Using `virtualenv` Module

`virtualenv` provides a handy set of tools to work with `venv` locally.

We will start with building our very own `venv`:

```bash
$ virtualenv venv
created virtual environment CPython3.7.5.final.0-64 in 170ms
  creator CPython3Posix(dest=/home/killswitch/Desktop/tools/PythonFundamentals/venv, clear=False, global=False)
  seeder FromAppData(download=False, pip=latest, setuptools=latest, wheel=latest, via=copy, app_data_dir=/home
  killswitch/.local/share/virtualenv/seed-app-data/v1.0.1)
  activators BashActivator,CShellActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator
```

We now can simply activate our `venv` using the following command:

```bash
$ source venv/bin/activate                                                                                        
(venv) $ python --version
Python 3.7.5
(venv) $ pip install requests
..::SNIP::..
(venv) $  pip freeze
..::SNIP::..
requests==2.23.0
urllib3==1.25.9
```

---
# Lab_3.py
**Tasking**
Using the new `virtualenv` command perform the following:
1. Go into the `01_python3_tooling_build_systems/` folder and create a venv using `virtualenv`
2. Activate the new shell using `source venv/bin/activate`
3. Using the custom `requirements.txt` file install these packages with `pip` 

**Testing your work**
**NOTE:** you should see Green `PASS` statements indicating you completed the lab
```bash
$ pip freeze 
$ python lab_3.py
```
