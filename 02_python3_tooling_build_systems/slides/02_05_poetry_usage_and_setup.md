---
marp: true
_class: lead
paginate: true
footer: 'Copyright (c) 2020 Obscurity Labs LLC.'
---

# Python Fun(damentals)
## Poetry Usage & Setup

**Alexander Rymdeko-Harvey**
Obscurity Labs
```text
* Directory Structure
* Config Files
```

![height:90px](https://obscuritylabs.com/wp-content/uploads/2019/11/OL-3d-landscape-positive-transparent.png)

---
# Python Poetry Package Manager

The venv module provides support for creating lightweight “virtual environments” with their own site directories, optionally isolated from system site directories.

* Near all the same capabilities of `pipenv`.
* Poetry comes with an exhaustive dependency resolver.
* Poetry either uses your configured `virtualenvs` or creates its own to always be isolated from your system.
* The most intuitive CLI on the market.
* Uses the newest PEP standards.
* Fully managed build systems and publishing of Python modules.
* The Package manager we will use going forward.

---
# Using `poetry`

`poetry` provides a handy set of tools to work with `virtualenvs` locally.

We will start by building our very own `env` as we did with other tools, the only difference is poetry will even scaffold the project for you:

```bash
$ poetry init                                                                                     
Author [None, n to skip]:  n
License []:  
Compatible Python versions [^3.7]:  

Would you like to define your main dependencies interactively? (yes/no) [yes] no
Would you like to define your development dependencies interactively? (yes/no) [yes] no
Generated file

[tool.poetry]
name = "01_python3_tooling_build_systems"
version = "0.1.0"
..::SNIP::..

Do you confirm the generation? (yes/no) [yes] yes
```

---
# Using `poetry` Cont.

We now can start adding packages to our new `env`:

```bash
$ poetry run python --version
poetry
```

We can also go into an interactive shell as we did with `pipenv`:
```bash
$ poetry shell
poetry/virtualenvs/01-python3-tooling-build-systems-3FZumH0Q-py3.7/bin/activate
(01-python3-tooling-build-systems-3FZumH0Q-py3.7) $
```

---
# Installing packages with `poetry`

We now can start adding packages to our new `env`:

```bash
$ poetry add requests
Using version ^2.23.0 for requests

Updating dependencies
Resolving dependencies... (0.2s)

Writing lock file


Package operations: 5 installs, 0 updates, 0 removals

  - Installing certifi (2020.4.5.1)
  - Installing chardet (3.0.4)
  - Installing idna (2.9)
  - Installing urllib3 (1.25.9)
  - Installing requests (2.23.0)
```
---
# Lab_5.py
**Tasking**
Using the new `poetry` command perform the following:
1. Go into the `02_python3_tooling_build_systems/` folder, notice we provided a `pyproject.toml` already.
2. Using `poetry` install `pytest`.
3. Ensure you have a `pyproject` is now updated with the new package.

**Testing your work**
**NOTE:** you should see Green `PASS` statements indicating you completed the lab
```bash
$ poetry shell
$ python lab_5.py
```