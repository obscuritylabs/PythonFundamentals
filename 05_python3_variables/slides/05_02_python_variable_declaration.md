---
marp: true
_class: lead
paginate: true
footer: 'Copyright (c) 2020 Obscurity Labs LLC.'
---

# Python Fun(damentals)
## Python Variable Declaration

**Alexander Rymdeko-Harvey**
Obscurity Labs
```text
* Variable Declaration
* Variable Documentation
```

![height:90px](https://obscuritylabs.com/wp-content/uploads/2019/11/OL-3d-landscape-positive-transparent.png)

   
---
# Python Variable Declaration 

Declaring a string example:
```python
>>> a = '1'
>>> b = '2'
>>> ab = a + b
>>> print(ab)
12
```

Declaring a int example:
```python
>>> a = 1
>>> b = 2
>>> ab = a + b
>>> print(ab)
3
```
*Notice what happen here?*

---
# Python Variable Declaration Cont.

Here is example using the `os` module in Python's core library.
```python
>>> import os
>>> currentPid = os.getpid()
>>> print(currentPid)
45034
```
- Variables can be used to capture module results
- Documentation is key to understanding what a module Returns
- This allows proper use

---
# Python Variable Documentation

If your lost its always best to READ THE DOCS. This will help you with what params, and return values and type.

https://docs.python.org/3/library/os.html
```python
os.getpid()
	Return the current process id.
```

---
# Lab_1.py
**Tasking**

Take the time to create two key variables, `currentProgram` which is a string that you define of the current program name. Second the use the python builtin os module to get current process id (PID) and declare it as `currentPid`. print both to the console using any method you would like to use.

**Testing your work**
**NOTE:** you should see Green `PASS` statements indicating you completed the lab
```bash
$ python lab_1.py
```

---
# Lab_2.py
**Tasking**

Take the time to create two variables that will be used in the future projects. import the module `sys` and use it to get the current modules loaded in the current namespace for debug purposes. Please name this variable `systemMod` and than convert this variable to a string which will be placed into `systemModS`.

**Testing your work**
**NOTE:** you should see Green `PASS` statements indicating you completed the lab
```bash
$ python lab_2.py
```