#!/usr/bin/env python
# HW02_ch03_ex03

# This exercise can be done using only the statements and other features we 
# have learned so far.

# (1) Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +

# Hint: to print more than one value on a line, you can print a 
# comma-separated sequence of values:

# print('+', '-')

# By default, print advances to the next line, but you can 
# override that behavior and put a space at the end, like this:

# print('+', end=' ')
# print('-')

# The output of these statements is '+ -'.

# A print statement with no argument ends the current line and 
# goes to the next line.



# (2) Write a function that draws a similar grid with four rows and four columns.
################################################################################
# Write your functions below:
def line():
	print ('+', end = ' ')
	print ('- - - -', end = ' ')

def endline():
	print ('+')

def do_twice(f):
	f()
	f()

def oneline():
	do_twice(line)
	endline()

def longline():
	do_twice(line)
	do_twice(line)
	endline()

def sidebar():
	x = ' ' * 9
	y = '|' + x + '|' + x + '|'
	print (y)

def do_four(f):
	f()
	f()
	f()
	f()

def grid():
	oneline()
	do_four(sidebar)
	oneline()
	do_four(sidebar)
	oneline()

def BigSidebar():
	x = ' ' * 9
	y = '|' + x + '|' + x + '|' + x + '|' + x + '|'
	print (y)

def BigGrid():
	longline()
	do_four(BigSidebar)
	longline()
	do_four(BigSidebar)
	longline()
	do_four(BigSidebar)
	longline()
	do_four(BigSidebar)
	longline()


# Write your functions above:
################################################################################
def main():
    """Call your functions within this function.
    When complete have two function calls in this function:
    two_by_two()
    four_by_four()
    """
    print("Hello World!")
    grid()
    BigGrid()


if __name__ == "__main__":
    main()