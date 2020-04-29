---
marp: true
_class: lead
paginate: true
footer: 'Copyright (c) 2020 Obscurity Labs LLC.'
---

# Python Fun(damentals)
## Python Variable Memory

**Alexander Rymdeko-Harvey**
Obscurity Labs
```text
* Variables
* Variable Memory
```

![height:90px](https://obscuritylabs.com/wp-content/uploads/2019/11/OL-3d-landscape-positive-transparent.png)

---

# Python Variables
Its important to understand C/C++ principles first, to understand what makes Python variables so easy to work with. Lets take the following example in C:
```c
/* variable definition: */
char str[50] = "Better know what im doing";
```
Now in Python, notice we dont declare it as a char or need size?
```python
a = 'Yea.. no size here'
```

---
# Python Variable Memory
The previous example works because:
- Python variables are nothing but reserved memory locations
- Based on variable type the Python interpreter allocates memory
- Declaration happens automatically when you assign a value to the variable
- This can easily be changed on the fly, expanded or shrunk
- This is the beauty of an object oriented non-statically typed language. 

---
# Python Variable Memory Cont.
Here is a example of a C program accessing memory ptr locations.
```c
#include <stdio.h>
#include <stdlib.h>
void main(void)

{
int var = 34;                                                                            
int *ptr;
ptr = &var;
printf("\nDirect access, 
	variable var value = var = %d", var);
printf("\nIndirect access, 
	variable var value = *ptr = %d", *ptr);
printf("\n\nThe memory 
	address of variable var = &var = %p", &var);
printf("\nThe memory 
	address of variable var = ptr = %p\n", ptr);
}
```
---

# Python Variable Memory Cont.
Here is a snipt of Python code I used to access `ptr` locations in memory:
```python
>>> a = 'alex'
>>> id(a)
4477448064
>>> hex(id(a))
'0x10ae06f80'
```
`id(object)`
	Return the “identity” of an object. This is an integer which is guaranteed to be unique and constant for this object during its lifetime. Two objects with non-overlapping lifetimes may have the same id() value.
    
---
# So what? 
1) The Python implementation should not be tied to a particular platform. It’s okay if some functionality is not always available, but the core should work everywhere.
2) Since most modern OS are written in C, compilers/interpreters for modern high-level languages are also written in C. Python is not an exception - its most popular/"traditional" implementation is called **CPython and is written in C**
3) PEP 20 -- The Zen of Python - https://www.python.org/dev/peps/pep-0020/  
