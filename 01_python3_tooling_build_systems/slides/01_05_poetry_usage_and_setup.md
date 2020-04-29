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

* Each virtual environment has its own Python binary.
    * which matches the version of the binary that was used to create this environment.
* Can have its own independent set of installed Python packages in its site directories.
* Prevents you from destroying your local development environment.
* Buys you the ability to test, run and build code in a controlled way.
* Comes built in with Python3
* Very low level and root of many build system tools (pipenv, Poetry etc.)