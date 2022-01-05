#!/usr/bin/env python
# coding: utf-8

# # Akshay Pawar MT2024

# # Q.1

# In[6]:


# Python Program to find Surface Area and volume of Cuboid

# inputs
length = 30
width = 20
height = 15

# Calculate the Surface Area
Surface_Area = 2 * (length * width + length * height + width * height)

# Calculate the Volume
Volume = length * width * height

 # Calculate the biggest face
a = length*width
b = width*height
c = height*length
def maximum(a, b, c):
    list = [a, b, c]
    return max(list)

# FInal output
print("\n The Surface Area of a Cuboid = %.2f " %Surface_Area)
print(" The Volume of a Cuboid = %.2f" %Volume)
print("Area of one of the biggest faces is ", maximum(a, b, c),"cm²")


# # Q.2

# In[8]:


length_1 = 30
length_2 = 40
length_3 = 50
width = 20
height = 15

# Calculate the Surface Area
Surface_Area_1 = 2 * (length_1 * width + length * height + width * height)
Surface_Area_2 = 2 * (length_2 * width + length * height + width * height)
Surface_Area_3 = 2 * (length_3 * width + length * height + width * height)

# Calculate the Volume
Volume_1 = length_1 * width * height
Volume_2 = length_2 * width * height
Volume_3 = length_3 * width * height

 # Calculate the biggest face with length_1
a_1 = length_1*width
b_1 = width*height
c_1 = height*length_1
def maximum(a_1, b_1, c_1):
    list = [a_1, b_1, c_1]
    return max(list)

# Calculate the biggest face with length_2
a_2 = length_2*width
b_2 = width*height
c_2 = height*length_2
def maximum(a_2, b_2, c_2):
    list = [a_2, b_2, c_2]
    return max(list)

# Calculate the biggest face with length_3
a_3 = length_3*width
b_3 = width*height
c_3 = height*length_3
def maximum(a_3, b_3, c_3):
    list = [a_3, b_3, c_3]
    return max(list)

# FInal output
#for length of 30cm
print("\n The Surface Area of a Cuboid = %.2f " %Surface_Area_1)
print(" The Volume of a Cuboid = %.2f" %Volume_1)
print("Area of one of the biggest faces is ", maximum(a_1, b_1, c_1),"cm²")

#for length of 40cm
print("\n The Surface Area of a Cuboid = %.2f " %Surface_Area_2)
print(" The Volume of a Cuboid = %.2f" %Volume_2)
print("Area of one of the biggest faces is ", maximum(a_2, b_2, c_2),"cm²")

#for length of 50cm
print("\n The Surface Area of a Cuboid = %.2f " %Surface_Area_3)
print(" The Volume of a Cuboid = %.2f" %Volume_3)
print("Area of one of the biggest faces is ", maximum(a_3, b_3, c_3),"cm²")


# # Q.3 Self-learning activity
Unit Test in Python:

If you have a fancy modern car, it will tell you when your light bulbs have gone. It does this using a form of unit test.

A unit test is a smaller test, one that checks that a single component operates in the right way. A unit test helps you to isolate what is broken in your application and fix it faster.

You have just seen two types of tests:

An integration test checks that components in your application operate with each other.
A unit test checks a small component in your application.

There is a module in Python’s standard library called unittest which contains tools for testing your code. Unit testing checks if all specific parts of your function’s behavior are correct, which will make integrating  them together with other parts much easier.

Test case is a collection of unit tests which together proves that a  function works as intended, inside a full range of situations in which that function may find itself and that it’s expected to handle. Test case should consider all possible kinds of input a function could receive from users, and therefore should include tests to represent each of these situations.

Passing a test
Here’s a typical scenario for writing tests:

First you need to create a test file. Then import the unittest module, define the testing class that inherits from unittest.TestCase, and lastly, write a series of methods to test all the cases of your function’s behavior.

Failing a test
To show you what a failing test looks like I’m going to modify a  formatted_name() function by including a new middle name argument.
In the output you will see information that will tell you all you need to know where the test fails:

First item in the output is the Error telling you that at least one test in test case resulted in an error.
Next you’ll see the file and method in which the error occurred.
After that you will see the line in which the error occurred.
And what kind of error it is, in this case we are missing 1 argument “middle_name”.
You will also see the number of run tests, the time needed for the tests to  complete, and a textual message that represents the status of the tests with number of errors that occurred.Python Profilers:

Today, there are so many of areas where you write code ranging from basic conditional logics to complex websites, apps, algorithms, etc. The main aspect while writing any code, especially when deploying, is that it should consume the lowest computational time and cost.

This is especially important when you run code on cloud services like AWS, Google Cloud or Azure, where there is a defined cost associated with the usage of computing resources. If you have two pieces of code that give the same result, the one that takes the least time and resource is usually chosen.

Introduction to cProfile
cProfile is a built-in python module that can perform profiling. It is the most commonly used profiler currently.

But, why cProfile is preferred?

It gives you the total run time taken by the entire code.
It also shows the time taken by each individual step. This allows you to compare and find which parts need optimization
cProfile module also tells the number of times certain functions are being called.
The data inferred can be exported easily using pstats module.
The data can be visualized nicely using snakeviz module. Examples come later in this post.

The cProfile profiler is one implementation of the Python profiling interface. It measures the time spent within functions and the number of calls made to them.

Note: The timing information should not be taken as absolute values, since the profiling itself could possibly extend the run time in some cases.

Run the following command to profile the code:

Replace python scatter.py with

python -m cProfile -o output.pstats scatter.py
in your Slurm script or when running interactively. Additional arguments can be passed to the scatter.py at the end if needed.

Notice the two options in the above command.

-m cProfile : the -m option specifies the python module to run as a script - this allows us to run cProfile from the command-line
-o output.pstats : the -o option specifies that the profiling results be written to the named file
If you leave out these options the code will just run normally.

Visualising the profiling output with gprof2dot
Note: You will need programs gprof2dot and dot, which are available on Mahuika and Maui. On other systems, use conda install gprof2dot to install gprof2dot and conda install graphviz to install Graphviz which provides the dot command.

Run gprof2dot to generate a PNG image file:

gprof2dot --colour-nodes-by-selftime -f pstats output.pstats | \
    dot -Tpng -o output.png
On Maui, generate an EPS image

gprof2dot --colour-nodes-by-selftime -f pstats output.pstats | \
    dot -Teps -o output.eps
as you would otherwise get message Format: "png" not recognized.

Now view output.png with the command display output.png on Mahuika (or display output.eps on Maui) if you have enabled X11-forwarding in your ssh command. Alternatively, you can copy the file your local machine and open it there.