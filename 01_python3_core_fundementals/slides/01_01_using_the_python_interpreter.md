---
marp: true
_class: lead
paginate: true
footer: 'Copyright (c) 2020 Obscurity Labs LLC.'
---

# Python Fun(damentals)
## Using the Python Interperter

**Alexander Rymdeko-Harvey**
Obscurity Labs
```text
* Quick Intro
* Live walkthrough
```

![height:90px](https://obscuritylabs.com/wp-content/uploads/2019/11/OL-3d-landscape-positive-transparent.png)

---
# How do you run these Python things you speak of?

A couple of key things to keep in mind when we talk about building Python applications:

* The Python **interactive** interpreter - A tool within the Python project
* Running code interactively in the interpreter - Live
* Running code directly in the interpreter - CLI arguments
* Running code directly with the Python binary - Byte compilation `-> exec()`

---
# Starting the Python Interpreter

On your, host CLI run the `python` command an interactive TTY shell will spawn and is ready for direct access to Python!

```Python
$ python3
Python 3.7.5 (default, Apr 19 2020, 20:18:17) 
[GCC 9.2.1 20191008] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 

```

Or you can even pass your Python code directly on the CLI:

```Python
$ python3 -c "print('hello world')"
hello world
```

---
# Lab 1
**Tasking**
Live instruction on opening the Python interpreter.