---
marp: true
_class: lead
paginate: true
footer: 'Copyright (c) 2020 Obscurity Labs LLC.'
---

# Python Fun(damentals)
## Python Boolean Types

**Alexander Rymdeko-Harvey**
Obscurity Labs
```text
* bool
```
![height:90px](https://obscuritylabs.com/wp-content/uploads/2019/11/OL-3d-landscape-positive-transparent.png)

---
# What Are Boolean's

* Booleans represent one of two values: `True` or `False`.
* In programming you often need to know if an expression is `True` or `False`.
* You can evaluate any expression in Python, and get one of two answers, `True` or `False`.
* When you compare two values, the expression is evaluated and Python returns the Boolean answer.
* Used heavy in logic flow.


---
# Boolean Operations

| Operation |            Result             |
| --------- | :---------------------------: |
| <, <=, >=, > | comparison operators |
| ==, !=, is, is not, in | comparison operators (continue) |
| not in    | comparison operators (continue) |
| not   | boolean NOT |
| and    | boolean AND |
| or    | boolean OR |
| bool() | type check |

---
# Using Booleans
Using the python interpreter we can perform live comparison operations:

```Python
Python 3.7.5 (default, Apr 19 2020, 20:18:17) 
[GCC 9.2.1 20191008] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 'hi' == 'hi'
True

>>> 5 == (3 + 2)   # Is five equal 5 to the result of 3 + 2?
True

>>> print(bool("Hello World"))
print(bool("Hello World"))
```

## Why?

---
# Lab 1 - Familiarization
**Tasking**
Using the new `python` command perform the following get familiar with `bool` types:
1. Perform a basic compare operation ex. `'hi' == 'hi'`
2. Perform a basic `in` operation ex. `'hi' in 'hi'`
