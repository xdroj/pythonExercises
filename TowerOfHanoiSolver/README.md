Tower of Hanoi Puzzle Solver (Python)
Project Overview
This project implements a solution to the classic Tower of Hanoi puzzle using Python. The Tower of Hanoi is a mathematical game or puzzle that consists of three rods and a number of disks of different sizes, which can slide onto any rod. The puzzle starts with the disks in a neat stack in ascending order of size on one rod, the smallest at the top, thus making a conical shape.

The objective of the puzzle is to move the entire stack from the source rod to another rod, obeying the following simple rules:

Only one disk can be moved at a time.

Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.

No disk may be placed on top of a smaller disk.

This implementation focuses on the elegant recursive solution to the problem.

Features
Recursive Algorithm: Solves the Tower of Hanoi puzzle using its natural recursive definition.

Disk Movement Simulation: Accurately simulates the movement of disks between the three rods.

Configurable Disks: Easily adjust the NUMBER_OF_DISKS variable to solve for different puzzle sizes.

Step-by-Step Output: Prints the state of the rods after each significant disk transfer, allowing you to follow the solution.

How It Works (Recursive Logic)
The move function uses recursion to break down the problem for n disks into three sub-problems:

Move n-1 smaller disks from the source rod to the auxiliary rod (using the target as a temporary).

Move the largest (n-th) disk from the source rod to the target rod.

Move the n-1 smaller disks from the auxiliary rod to the target rod (using the source as a temporary).

The base case for the recursion is when n (the number of disks to move) is 0 or less, at which point no action is taken.

Setup and Running the Project
To run this project:

Save the code: Copy the entire Python code into a file named hanoi_solver.py (or any other .py extension).

Open a terminal or command prompt.

Navigate to the directory where you saved the file.

Run the script:

Bash

python hanoi_solver.py
The output will display the step-by-step movements of the disks and the state of the rods (A, B, C) after each move.

Concepts Demonstrated
This project is an excellent demonstration of several core programming concepts:

Recursion: Understanding base cases and recursive calls for problem-solving.

Functions: Defining and calling functions with multiple parameters.

List Manipulation: Using methods like .append() and .pop() to modify lists, simulating disk placement and removal.

Global Variables: Using global variables (A, B, C, NUMBER_OF_DISKS) to manage the state of the puzzle.

Parameter Passing: Passing mutable objects (lists) directly to functions.

Problem Decomposition: Breaking down a complex problem into smaller, manageable sub-problems.