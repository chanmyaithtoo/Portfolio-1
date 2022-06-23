
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item for QUTC's teaching unit
#  ITD104, "Building IT Systems", C1 2022.  By submitting
#  this code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
student_number = 11178931 # put your student number here as an integer
student_name   = "Chan Myait Htoo" # put your name here as a character string
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  LOCKDOWN
#
#  This assessment item tests your skills at processing data stored in
#  lists, creating reusable code and following instructions to display
#  a complex visual image.  The incomplete Python program below is
#  missing a crucial function, "track_entities".  You are required to
#  complete this function so that when the program runs it fills
#  a grid with various symbols, using data stored in a list to
#  determine which symbols to draw and where.  See the various
#  "client briefings" in Blackboard for full details.
#
#  Note that this assessable assignment is in multiple parts,
#  simulating incremental release of instructions by the client.
#  This single template file will be used for all parts and you will
#  submit your final solution as a single Python 3 file only, whether
#  or not you complete all requirements for the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You must NOT change
# any of the code in this section.
#

# Import standard Python modules needed to complete this assignment.
# You should not need to use any other modules for your solution.
# In particular, your solution must NOT rely on any non-standard
# Python modules that need to be downloaded and installed separately,
# because the markers will not have access to such modules.
from turtle import *
from math import *
from random import *
from sys import exit as abort
from os.path import isfile

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values unless
# instructed.
cell_size = 100 # pixels (default is 100)
grid_width = 8 # squares (default is 8)
grid_height = 7 # squares (default is 7)
x_margin = cell_size * 2.5 # pixels, the size of the margin left/right of the grid
y_margin = cell_size // 2 # pixels, the size of the margin below/above the grid
window_height = grid_height * cell_size + y_margin * 2
window_width = grid_width * cell_size + x_margin * 2
small_font = ('Arial', cell_size // 5, 'normal') # font for the coords
big_font = ('Arial', cell_size // 4, 'normal') # font for any other text

# Validity checks on grid size - do not change this code
assert cell_size >= 80, 'Cells must be at least 80x80 pixels in size'
assert grid_width >= 7, 'Grid must be at least 7 squares wide'
assert (grid_height >= 5) and (grid_height % 2 != 0), \
       'Grid must be at least 5 squares high and height must be odd'

#
#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# manage the drawing canvas for your image.  Do NOT change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image
def create_drawing_canvas(bg_colour = 'light grey',
                          line_colour = 'slate grey',
                          draw_grid = True,
                          label_spaces = True): # NO! DON'T CHANGE THIS!
    
    # Set up the drawing canvas with enough space for the grid and
    # spaces on either side
    setup(window_width, window_height)
    bgcolor(bg_colour)
    LGA_border_line_colour = 'red'
    LGA_border_line_width = 5

    # Draw as quickly as possible
    tracer(False)

    # Get ready to draw the grid
    penup()
    color(line_colour)
    width(2)

    # Determine the left-bottom coords of the grid
    left_edge = -(grid_width * cell_size) // 2 
    bottom_edge = -(grid_height * cell_size) // 2

    # Optionally draw the grid
    if draw_grid:

        # Draw the horizontal grid lines
        setheading(0) # face east
        for line_no in range(0, grid_height + 1):
            penup()
            goto(left_edge, bottom_edge + line_no * cell_size)
            pendown()
            forward(grid_width * cell_size)
            
        # Draw the vertical grid lines
        setheading(90) # face north
        for line_no in range(0, grid_width + 1):
            penup()
            # make the middle line different, to differentiate the LGAs
            if line_no == 4:
                goto(left_edge + line_no * cell_size, bottom_edge - (cell_size / 2))
                pendown()
                width(LGA_border_line_width)
                color(LGA_border_line_colour)
                forward((grid_height + 1) * cell_size)
                color(line_colour)
                width(2)
            else:
                goto(left_edge + line_no * cell_size, bottom_edge)
                pendown()
                forward(grid_height * cell_size)

        # Draw each of the labels on the x axis
        penup()
        y_offset = cell_size // 3 # pixels
        for x_label in range(0, grid_width):
            goto(left_edge + (x_label * cell_size) + (cell_size // 2), bottom_edge - y_offset)
            write(str(x_label + 1), align = 'right', font = small_font)

        # Draw each of the labels on the y axis
        penup()
        x_offset, y_offset = cell_size // 5, cell_size // 10 # pixels
        for y_label in range(0, grid_height):
            goto(left_edge - x_offset, bottom_edge + (y_label * cell_size) + (cell_size // 2) - y_offset)
            write(chr(y_label + ord('A')), align = 'center', font = small_font)

        # Mark the two "special" cells
        goto(-cell_size * grid_width // 2 + 0.5 * cell_size, 0)
        dot(cell_size // 6)
        goto(cell_size * grid_width // 2 - 0.5 * cell_size, 0)
        dot(cell_size // 6)

    # Optionally mark the blank spaces ... NO! YOU CAN'T CHANGE ANY OF THIS CODE!
    if label_spaces:
        # Left side
        goto(-((grid_width + 1.15) * cell_size) // 2, -(cell_size // 2))
        write('Draw the\ntwo states of\nyour first\nentity here', align = 'right', font = big_font)    
        # Right side
        goto(((grid_width + 1.15) * cell_size) // 2, -(cell_size // 2))
        write('Draw the\ntwo states of\nyour second\nentity here', align = 'left', font = big_font)    

    # Reset everything ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)

# End the program and release the drawing canvas to the operating
# system.  By default the cursor (turtle) is hidden when the
# program ends.  Call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor = True):
    tracer(True) # ensure any drawing still in progress is displayed
    if hide_cursor:
        hideturtle()
    done()
    
#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "track_entities" function.  ALL of your solution code
#  must appear in, or be called from, function "track_entities".  Do
#  NOT put any of your code in other parts of the program and do NOT
#  change any of the provided code except as allowed in the main
#  program below.
#

# WRITE WHAT THE PURPOSE OF THE FUNCTION IS
def track_entities(instruction):
    #Function to draw the square
    def draw_square(x_coord, y_coord):
        #Set the direction to east
        setheading(0)
        penup()
        fillcolor('white')
        pencolor('black')
        #Go to the specified location
        goto(x_coord, y_coord)
        pendown()
        #Set the length of the square
        square_length = 100
        #Set the number of times for turning angles
        num_turns = 4
        begin_fill()
        for turn in range(num_turns):
            forward(square_length)
            left(90)
        end_fill()
    
    def draw_branch(state, branch_len, leaf_color,trunk_color):
        #Set the depth
        depth = 5
        #Set the random angle before drawing subbranches
        turn_angle = randint(22, 26)
        turn_angle = 24
        #Set the size factor for the length of subbranches
        size_factor = uniform(0.6, 0.8)
        #Set the thickness of the branch
        thickness = branch_len // 10
        pensize(thickness)
        
        #Draw the leaf at the certain depth
        if (state) and (branch_len  < (depth * 2)):
            color(leaf_color)
            stamp()
            color(trunk_color)
    
        if branch_len > depth:
            #Draw the branch
            forward(branch_len)
            #Turn the turtle to the left to draw the left part of the branch
            left(turn_angle)
            #Begin to draw the left part of the sub branches
            draw_branch(state, branch_len * size_factor, leaf_color, trunk_color)
            #Turn to the turtle to the right to draw the right part of the branch
            right(turn_angle * 2)
            #Begin to draw the right part of the sub branches
            draw_branch(state, branch_len * size_factor, leaf_color, trunk_color)
            #Turn the turtle towards the junction point
            left(turn_angle)
            #Return to the junction
            backward(branch_len)
        
    # calculate the x_coordate to start drawing the trunk
    def start_location(x_coord):
        start_location_x = x_coord + 50
        return start_location_x
    
    #Function to draw the maple tree with two different states
    def draw_maple_tree(x_coord, y_coord, healthy_state):
        #Set the trunk size
        trunk_length = 27
        #Set the trunk color
        trunk_color = "brown"
        penup()
        #Go to the specified location
        goto(x_coord, y_coord)
        #Set the heading to the north
        setheading(90)
        pendown()
        #Set the speed to fast
        speed("fast")
        #Set the pencolor brown
        color()
        #Set the leaf color
        leaf_color = "yellow"
        #Call the function to draw the branch
        draw_branch(healthy_state,trunk_length,leaf_color,trunk_color)
        #Set the pen colour "black"
        pencolor("black")

    def draw_htanaung_tree(x_coord, y_coord, healthy_state):
        #Set the trunk size
        trunk_length = 27
        #Set the trunk color as red
        trunk_color = "yellow"
        pencolor("black")
        penup()
        #Go to the specified location 
        goto(x_coord, y_coord)
        #Set the heading to the north
        setheading(90)
        pendown()
        #Set the speed to fast
        speed("fast")
        #Set the pencolor brown
        color(trunk_color)
        #Set the leaf color
        leaf_color = "green"
        #Call the function to draw the branch
        draw_branch(healthy_state,trunk_length,leaf_color,trunk_color)
        #Set the pen colour "black"
        pencolor("black")
    
    #Function to write the label at the bottom of the square
    def write_lable(x_coord,y_coord,sentence):
        pencolor("black")
        penup()
        goto(x_coord, y_coord)
        setheading(0)
        pendown()
        write(sentence)

    #Draw the first square for the healthy maple tree
    healthy_maple_x = -600
    healthy_maple_y = 100
    draw_square(healthy_maple_x, healthy_maple_y)
    draw_maple_tree(start_location(healthy_maple_x), healthy_maple_y, healthy_state = True)
    write_lable(healthy_maple_x, healthy_maple_y - 30, "Healthy maple")

    #Draw the second square for the unhealthy maple tree
    unhealthy_maple_x = -600
    unhealthy_maple_y = -200
    draw_square(unhealthy_maple_x, unhealthy_maple_y)
    draw_maple_tree(start_location(unhealthy_maple_x), unhealthy_maple_y, healthy_state = False)
    write_lable(unhealthy_maple_x, unhealthy_maple_y - 30, "Unhealthy maple")

    #Draw the third square for the healthy htanaung tree
    healthy_htanaung_x = 500
    healthy_htanaung_y = 100
    draw_square(healthy_htanaung_x, healthy_htanaung_y)
    draw_htanaung_tree(start_location(healthy_htanaung_x), healthy_htanaung_y, healthy_state = True)
    write_lable(healthy_htanaung_x, healthy_htanaung_y - 30, "Healthy htanaung")

    #Draw the fourth square for the unhealthy htanaung tree
    unhealthy_htanaung_x = 500
    unhealthy_htanaung_y = -200
    draw_square(unhealthy_htanaung_x, unhealthy_htanaung_y)
    draw_htanaung_tree(start_location(unhealthy_htanaung_x), unhealthy_htanaung_y, healthy_state = False)
    write_lable(unhealthy_htanaung_x, unhealthy_htanaung_y - 30, "Unhealthy htanaung")

#---3-----------------------------------------------------------------#

    #Check the state of the entity
    def check_state(entities_states):
        states = []
        for state in entities_states:
            if state == "Healthy":
                states.append(True)
            else:
                states.append(False)
        return states
    
    #Calculate the location 
    def get_direction (instruction):
        direction = {
            "North": 90,
            "South": 270,
            "West": 180,
            "East": 0
        }
        return direction.get(instruction)
    
        
    
    # sample_data = [['Healthy', 'Unwell'],
    #                 ['Right entity', 'West', 4],
    #                 ['Left entity', 'North', 2],
    #                 ['Righ entity', 'South', 1],
    #                 ['Left entity', 'East', 4],
    #                 ['Right entity', 'West', 3],
    #                 ['Left entity', 'East', 2],
    #                 ['Left entity', 'North', 2],
    #                 ['Left entity', 'East', 1],
    #                 ['Left entity', 'East', 4],
    #                 ['Right entity', 'West', 4],
    #                 ['Left entity', 'North', 1],
    #                 ['Left entity', 'East', 1],
    #                 ['Right entity', 'South', 2],
    #                 ['Right entity', 'South', 1],
    #                 ['Left entity', 'East', 3],
    #                 ['Left entity', 'West', 7],
    #                 ['Left entity', 'South', 1]]


    sample_data = instruction
    maple_state, htanaung_state = check_state(sample_data[0])
    step = 100
    max_x_coord = 400
    max_y_coord = 350
    #Draw the home location for the maple tree
    home_maple_x = -400
    home_maple_y = -50
    home_maple_coord = (home_maple_x, home_maple_y)
    draw_square(home_maple_x, home_maple_y)
    draw_maple_tree(start_location(home_maple_x), home_maple_y, maple_state)
    current_maple_location = home_maple_coord

    #Draw the home location for the htanaung tree
    home_htanaung_x = 300
    home_htanaung_y = - 50
    home_htanaung_coord = (home_htanaung_x, home_htanaung_y)
    draw_square(home_htanaung_x, home_htanaung_y)
    draw_htanaung_tree(start_location(home_htanaung_x), home_htanaung_y, htanaung_state)
    current_htanaung_location = home_htanaung_coord

    #The loop iterate through the instances of data and draw the entities
    #according to the instruction and check whether the entity is in the grid or not.
    for entity_type, direction, num_cells in sample_data[1:]:
        if entity_type == 'Left entity':
            for cell in range(num_cells):
                penup()
                goto(current_maple_location)
                setheading(get_direction(direction))
                forward(step)
                test_maple_location = pos()
                test_maple_x, test_maple_y = round(test_maple_location[0]), round(test_maple_location[1])
                #If the entity is at the home location, skip it
                if (test_maple_x, test_maple_y) == home_maple_coord or (test_maple_x, test_maple_y) == home_htanaung_coord:
                    current_maple_location = test_maple_location
                    continue
                #If the entity is at the border, stop it
                if test_maple_y == max_y_coord or test_maple_x == max_x_coord:
                    continue
                #If the entity is within the grid, change the state and draw the entity depending on the instruction.
                if (abs(test_maple_x) <= max_x_coord) and (abs(test_maple_y) <= max_y_coord):
                    if (test_maple_x == 0 and maple_state):
                        maple_state = htanaung_state
                    draw_square(test_maple_x, test_maple_y)
                    draw_maple_tree(start_location(test_maple_x), test_maple_y, maple_state)
                    current_maple_location = test_maple_location
        else:
            for cell in range(num_cells):
                penup()
                goto(current_htanaung_location)
                #print(pos())
                setheading(get_direction(direction))
                forward(step)
                test_htanaung_location = pos()
                test_htanaung_x, test_htanaung_y = round(test_htanaung_location[0]), round(test_htanaung_location[1])
                #If the entity is at the home location, skip it
                if (test_htanaung_x, test_htanaung_y) == home_htanaung_coord or (test_htanaung_x, test_htanaung_y) == home_maple_coord:
                    current_htanaung_location = test_htanaung_location
                    continue
                #If the entity is at the border, stop it
                if test_htanaung_y == max_y_coord or test_htanaung_x == max_x_coord:
                    continue
                #If the entity is within the grid, change the state and draw the entity depending on the instruction.
                if (abs(test_htanaung_x) <= max_x_coord) and (abs(test_htanaung_y) <= max_y_coord):
                    if (test_htanaung_x == -100 and htanaung_state):
                        htanaung_state = maple_state
                    draw_square(test_htanaung_x, test_htanaung_y)
                    draw_htanaung_tree(start_location(test_htanaung_x), test_htanaung_y, htanaung_state)
                    current_htanaung_location = test_htanaung_location
            
    
#-----Initialisation Steps-------------------------------------------#
#
# This code checks that the programmer's identity has been provided
# and whether or not the data generation function is available.  You
# should NOT change any of the code in this section.
#

# Confirm that the student has declared their authorship
if not isinstance(student_number, int):
    print('\nUnable to run: No student number supplied',
          '(must be an integer)\n')
    abort()
if not isinstance(student_name, str):
    print('\nUnable to run: No student name supplied',
          '(must be a character string)\n')
    abort()

### Define the function for generating data sets, using the
### client's data generation function if available, but
### otherwise creating a dummy function that returns an empty
### list
if isfile('entity_data.py'):
    print('\nData module found\n')
    from entity_data import entity_actions
    def actions(new_seed = None):
        seed(new_seed)
        return entity_actions(grid_width, grid_height)
else:
    print('\nNo data module available!\n')
    def actions(dummy_parameter = None):
        return []

#
#--------------------------------------------------------------------#



#-----Main Program to Create Drawing Canvas--------------------------#
#
# This main program sets up the canvas, ready for you to start
# drawing your solution.  Do NOT change any of this code except
# as indicated by the comments marked '*****'.  Do NOT put any of
# your solution code in this area.
#

# Set up the drawing canvas
# ***** You can change the background and line colours, and choose
# ***** whether or not to draw the grid and other elements, by
# ***** providing arguments to this function call
create_drawing_canvas(label_spaces = False) 

# Control the drawing speed
# ***** Change the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** forever while the cursor moves slooooowly around the screen
tracer(False)

# Give the drawing canvas a title
# ***** Replace this title with a description of your solution's
# ***** overall theme
title("Trees in the park")

# Call the student's function to process the data set
# ***** While developing your program you can call the
# ***** "actions" function with a fixed seed for the
# ***** random number generator, but your final solution must
# ***** work with "actions()" as the argument to "track_entities",
# ***** i.e., for any data set that can be returned by
# ***** calling function "actions" with no seed.
track_entities(actions()) # <-- no argument for "actions" when assessed

# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible when the program
# ***** terminates as a debugging aid
release_drawing_canvas() # ('light grey', 'slate grey', True, False)

#
#--------------------------------------------------------------------#
