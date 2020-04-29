---
marp: true
_class: lead
paginate: true
footer: 'Copyright (c) 2020 Obscurity Labs LLC.'
---

# Python Fun(damentals)
## Defining Functions

**Alexander Rymdeko-Harvey**
Obscurity Labs
```text
* functions
```

![height:90px](https://obscuritylabs.com/wp-content/uploads/2019/11/OL-3d-landscape-positive-transparent.png)

---
# What is a Function

1) A function is a block of code which only runs when it is called.
2) You can pass data known as parameters into a function.
3) A function can return data


---
# Creating Hello World

We create a function by using the `def` keyword. This tells python the following statement is a function.

* Functions are INDENT sensitive. YOU must ensure consistent indents (Tab or Space)
* PEP recommends 4 spaces or 1 tab which a IDE will convert to 4 spaces.

```python
def hi(): # notice the def
  print("hi!")

def hi2(): # notice the def
  return "hi!" # this returns a string type
```

---
# Adding Arguments

When we create a function we can take in values to be processed or used by the function:

```python
def hi(string): # notice the def
  print(string)

def hi2(string): # notice the arg
  string = string + " fun"
  return string # this returns the value
```

---
# Lab_1.py
**Tasking**
Using the new `poetry` command perform the following:
1. Go into the `06_python3_flow_control/` folder and open `lab_1.py`
2. Add a function called `hello_world() that takes in a string
3. return the value of the argument as a return value

**Testing your work**
**NOTE:** you should see Green `PASS` statements indicating you completed the lab
```bash
$ poetry shell
$ python lab_1.py
```
