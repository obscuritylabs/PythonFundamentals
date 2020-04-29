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
# Python `pipenv` build-system

Pipenv is a tool that aims to bring the best of all packaging worlds (bundler, composer, npm, cargo, yarn, etc.) to the Python world.

* You no longer need to use pip and virtualenv separately. They work together.
* Managing a requirements.txt file can be problematic, so Pipenv uses Pipfile and Pipfile.lock to separate abstract dependency declarations from the last tested combination.
* Hashes are used everywhere, always. Security. Automatically expose security vulnerabilities.
* Strongly encourage the use of the latest versions of dependencies to minimize security risks arising from outdated components.
* Give you insight into your dependency graph (e.g. `$ pipenv graph`).


---
# Using `pipenv`

`pipenv` provides a handy set of tools to work with `virtualenv` locally.

We will start with building our very own `env`:

```bash
$ pipenv --python 3
⠋created virtual environment CPython3.7.5.final.0-64 in 162ms
creator CPython3Posix(dest=/home/killswitch/.local/share/virtualenvs
  01_python3_tooling_build_systems-YCx-KAYf, clear=False, global=False)
  seeder FromAppData(download=False, pip=latest, setuptools=latest, wheel=latest, via=copy, app_data_dir=/home
  killswitch/.local/share/virtualenv/seed-app-data/v1.0.1)
activators BashActivator,CShellActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator

Virtualenv location: /home/killswitch/.local/share/virtualenvs/01_python3_tooling_build_systems-YCx-KAYf
requirements.txt found, instead of Pipfile! Converting…
Warning: Your Pipfile now contains pinned versions, if your requirements.txt did. 
We recommend updating your Pipfile to specify the "*" version, instead.
```

We now can simply activate our `pipenv` using the following command:

```bash
$ pipenv shell
(01_python3_tooling_build_systems-YCx-KAYf) $ python --version
```

---
# Installing packages with `pipenv`

`pipenv` provides a handy set of tools to work with `virtualenv` locally.

We will start with building our very own `env`:

```bash
$ pipenv --python 3
⠋created virtual environment CPython3.7.5.final.0-64 in 162ms
creator CPython3Posix(dest=/home/killswitch/.local/share/virtualenvs
  01_python3_tooling_build_systems-YCx-KAYf, clear=False, global=False)
  seeder FromAppData(download=False, pip=latest, setuptools=latest, wheel=latest, via=copy, app_data_dir=/home
  killswitch/.local/share/virtualenv/seed-app-data/v1.0.1)
activators BashActivator,CShellActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator

Virtualenv location: /home/killswitch/.local/share/virtualenvs/01_python3_tooling_build_systems-YCx-KAYf
requirements.txt found, instead of Pipfile! Converting…
Warning: Your Pipfile now contains pinned versions, if your requirements.txt did. 
We recommend updating your Pipfile to specify the "*" version, instead.
```

We now can simply activate our `pipenv` using the following command:

```bash
$ pipenv shell
(01_python3_tooling_build_systems-YCx-KAYf) $ python --version
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
