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
* control flow
```

![height:90px](https://obscuritylabs.com/wp-content/uploads/2019/11/OL-3d-landscape-positive-transparent.png)

---
# What is a Control Flow

The programs we have written and used up until this point have be a series of code that are executed in a state of flow (top down). We need to now add logic to our programs.

Take this scenario for example: we need to take in a book page and return the text for this page but we have many different pages. And if they select a missing page we need to warn the user. How do we do this?

This is achieved using control flow statements. There are three control flow statements in Python - if, for and while.

---
# Creating a basic `if` Statement

```python
page = int(input('Enter an integer : '))

if page == 1:
    print('Page 1 text: Hi alex)
else:
    print(f'Page {page} is missing)

print("Done!)
```

---
# Creating a basic `if` Statement with Multiple Pages

```python
page = int(input('Enter an integer : '))

if page == 1:
    print('Page 1 text: Hi alex')
elif page == 2:
    print(f'Page {page} text: Hi from page 2')
elif page > 2:
    print(f'Page {page} is larger than pages in the db')
else: # anyone know how we could get here?
    print(f'Page {page} does not exist, how did we get here?')
print("Done!)
```

---
# Lab_2.py
**Tasking**
Using the new `poetry` command perform the following:
1. Go into the `06_python3_flow_control/` folder and open `lab_2.py`
2. Add a function called `hello_world(value)` that takes in a `int`
3. Create a if statement in this function that returns the string `pass` if passed the `int` `5` 
4. otherwise the function should return `fail`

**Testing your work**
**NOTE:** you should see Green `PASS` statements indicating you completed the lab
```bash
$ poetry shell
$ python lab_2.py
```

