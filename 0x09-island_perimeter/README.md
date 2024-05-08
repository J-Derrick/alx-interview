0x09. Island Perimeter
======================

	- Algorithm

	- Python

-  Weight: 1
- Project will start May 6, 2024 6:00 AM, must end by May 10, 2024 6:00 AM
- Checker was released at May 7, 2024 6:00 AM
- An auto review will be launched at the deadline

For the “0. Island Perimeter” project, you will need to apply your knowledge of algorithms, data structures (specifically matrices or 2D lists), and iterative or conditional logic to solve a geometric problem within a grid context. The goal is to calculate the perimeter of a single island in a grid, where the grid is represented by a 2D array of integers. Understanding how to navigate and analyze 2D arrays and apply logical operations to determine the conditions for perimeter calculation is crucial for this task.

Concepts Needed:
-----------------

1. 2D Arrays (Matrices):

	- Accessing and iterating over elements in a 2D array.
	- Understanding how to navigate through adjacent cells (horizontally and vertically).

2. Conditional Logic:

	- Applying conditions to determine whether a cell contributes to the perimeter of the island.

3. Counting Techniques:

	- Developing a method to count the edges that contribute to the island’s perimeter.

4. Problem-Solving Strategies:

	- Breaking down the problem into smaller tasks, such as identifying land cells and calculating their contribution to the perimeter.

5. Python Programming:

	- Nested loops for iterating over grid cells.
	- Conditional statements to check the status of adjacent cells.

Resources:
----------

**- Python Official Documentation:**

	- [Nested Lists](https://intranet.alxswe.com/rltoken/8SPalOgoGDWQChVbct0p1g): Understanding how to work with lists within lists in Python.
**- GeeksforGeeks Articles:**

	- [Python Multi-dimensional Arrays](https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/): A guide to working with 2D arrays in Python effectively.

**- TutorialsPoint:**

	- [Python Lists](https://intranet.alxswe.com/rltoken/TZ8UtQaRxN5cFf8c1TB-rw): Explains how to create, access, and manipulate lists in Python, which is essential for working with a grid.

**- YouTube Tutorials:**

	- [Python 2D arrays and lists](https://intranet.alxswe.com/rltoken/H7SwlI_XYDpwYonNYKXQfg)

By understanding these concepts and utilizing the provided resources, you will be equipped to approach the problem methodically. You’ll need to iterate over the grid, apply logical operations to identify the perimeter of the island, and account for the specific conditions described in the task. This project not only tests your algorithmic thinking but also reinforces your ability to manipulate data structures and apply logical reasoning to solve problems.

Additional Resources
---------------------

- [Mock Technical Interviews](https://intranet.alxswe.com/rltoken/9ZYjQgC9HvOLZiHxmgd89Q)

Requirements
------------

### General

-   Allowed editors: `vi`, `vim`, `emacs`
-   All your files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
-   All your files should end with a new line
-   The first line of all your files should be exactly `#!/usr/bin/python3`
-   A `README.md` file, at the root of the folder of the project, is mandatory
-   Your code should use the `PEP 8` style (version 1.7)
-   You are not allowed to import any module
-   All modules and functions must be documented
-   All your files must be executable

Tasks
-----

### 0\. Island Perimeter

mandatory

Create a function `def island_perimeter(grid):` that returns the perimeter of the island described in `grid`:

-   `grid` is a list of list of integers:
    -   0 represents water
    -   1 represents land
    -   Each cell is square, with a side length of 1
    -   Cells are connected horizontally/vertically (not diagonally).
    -   `grid` is rectangular, with its width and height not exceeding 100
-   The grid is completely surrounded by water
-   There is only one island (or nothing).
-   The island doesn't have "lakes" (water inside that isn't connected to the water surrounding the island).

```
guillaume@ubuntu:~/0x09$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))

guillaume@ubuntu:~/0x09$
guillaume@ubuntu:~/0x09$ ./0-main.py
12
guillaume@ubuntu:~/0x09$

```
**-----------SOLUTION-----------**

```
#!/usr/bin/python3
"""
Island Perimeter
"""

def island_perimeter(grid):
    """
     returns the perimeter of the island described in grid
    :param grid:
    :return:
    """
    area = 0
    for row in grid + list(map(list, zip(*grid))):
        for i1, i2 in zip([0] + row, row + [0]):
            area += int(i1 != i2)
    return area
```

**----------------CODE EXPLANATION-------------------**

- It uses a clever trick to calculate the perimeter by iterating over the rows of the grid and adding the number of transitions from land (1) to water (0) for each row, as well as the number of transitions between rows.

Code Breakdown:

`grid + list(map(list, zip(*grid)))` concatenates the original grid with its transpose. This is done to efficiently iterate through both rows and columns of the grid in a single loop.

`for row in grid + list(map(list, zip(*grid)))`: iterates through each row of the combined grid (original grid and its transpose).

`for i1, i2 in zip([0] + row, row + [0])`: iterates through each pair of adjacent elements in the row, including the beginning and end.

`area += int(i1 != i2)` increments the area by 1 whenever there is a transition from land (1) to water (0) or vice versa, which effectively counts the perimeter.

This code is a great example of utilizing the properties of the grid to simplify the perimeter calculation and avoid nested loops. It produces the same output as the previous code you provided, which is 12 for the given example.
