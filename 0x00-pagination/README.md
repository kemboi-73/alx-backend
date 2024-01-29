# ALX Backend - Pagination Project

## Overview
This repository contains the code for a Python project focused on implementing pagination in the context of a database of popular baby names. The project is divided into three tasks, each building upon the previous one, with a focus on enhancing pagination features.

### Curriculum
#### Short Specializations
- **Average:** 67.69%

#### 0x00. Pagination
- **Back-end**
- **Author:** Emmanuel Turlay, Staff Software Engineer at Cruise
- **Weight:** 1
- **Project Period:** Jan 25, 2024 6:00 AM - Jan 30, 2024 6:00 AM
- **Checker Release:** Jan 26, 2024 12:00 PM
- **Auto Review:** Triggered at the deadline

### Resources
- **Read or Watch:**
  - [REST API Design: Pagination](#)
  - [HATEOAS](#)

### Learning Objectives
By the end of this project, participants are expected to be able to explain the following concepts without external assistance:
- How to paginate a dataset with simple page and page_size parameters.
- How to paginate a dataset with hypermedia metadata.
- How to paginate in a deletion-resilient manner.

### Requirements
- All files interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7).
- All files end with a new line.
- The first line of all files is exactly `#!/usr/bin/env python3`.
- A `README.md` file at the root of the project folder is mandatory.
- Code follows the `pycodestyle` style (version 2.5.*).
- File length is tested using `wc`.
- All modules have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`).
- All functions have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`).
- Functions and coroutines must be type-annotated.

### Setup
- Data file: `Popular_Baby_Names.csv` (use this data file for the project).

## Tasks

### 0. Simple Helper Function
- Write a function named `index_range` that takes two integer arguments: `page` and `page_size`.
- The function should return a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those pagination parameters.
- Page numbers are 1-indexed.

Example:
```python
# Usage
index_range = __import__('0-simple_helper_function').index_range

res = index_range(1, 7)
print(type(res))
print(res)
```
Output:
```python
<class 'tuple'>
(0, 7)
```

[Repository File: 0x00-pagination/0-simple_helper_function.py](#)

### 1. Simple Pagination
- Copy `index_range` from the previous task and implement a `Server` class with a method named `get_page`.
- `get_page` takes two integer arguments: `page` with a default value of 1 and `page_size` with a default value of 10.
- Use `assert` to verify that both arguments are integers greater than 0.
- Use `index_range` to find the correct indexes to paginate the dataset correctly and return the appropriate page of the dataset.
- If the input arguments are out of range for the dataset, an empty list should be returned.

Example:
```python
# Usage
Server = __import__('1-simple_pagination').Server

server = Server()

try:
    should_err = server.get_page(-10, 2)
except AssertionError:
    print("AssertionError raised with negative values")

# Additional usage examples
# ...

```

[Repository File: 0x00-pagination/1-simple_pagination.py](#)

### 2. Hypermedia Pagination
- Replicate code from the previous task.
- Implement a `get_hyper` method that takes the same arguments as `get_page` and returns a dictionary containing hypermedia information.

Example:
```python
# Usage
Server = __import__('2-hypermedia_pagination').Server

server = Server()

print(server.get_hyper(1, 2))
# Additional usage examples
# ...
```

[Repository File: 0x00-pagination/2-hypermedia_pagination.py](#)

### 3. Deletion-Resilient Hypermedia Pagination
- Implement a `get_hyper_index` method in the `Server` class with two integer arguments: `index` with a default value of `None` and `page_size` with a default value of 10.
- The method should return a dictionary with hypermedia information, considering deletion-resilient pagination.
- Use `assert` to verify that the index is in a valid range.
- If the user queries index 0, page_size 10, they will get rows indexed 0 to 9 included.
- If they request the next index (10) with page_size 10, but rows 3, 6, and 7 were deleted, the user should still receive rows indexed 10 to 19 included.

Example:
```python
# Usage
Server = __import__('3-hypermedia_del_pagination').Server

server = Server()

server.indexed_dataset()

try:
    server.get_hyper_index(300000, 100)
except AssertionError:
    print("AssertionError raised when out of range")

# Additional usage examples
# ...
```

[Repository File: 0x00-pagination/3-hypermedia_del_pagination.py](#)

## Copyright
Copyright © 2024 ALX, All rights reserved.
