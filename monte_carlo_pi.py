# -*- coding: utf-8 -*-
# Imports all the necessary libraries
"""This application approximates the PI value based on a Monte Carlo Simulation.
It asks for input from the user regarding on number of darts thrown."""
import math
import random
import numpy as np
import matplotlib.pyplot as plt

def gen_circle(radius=1, center_x=0, center_y=0, res=50):
    """Returns the points of coordinates [x,y] which lie on the circle
    with the radius radius and with the center specified at center = [x,y],
    with the resolution res"""
    xcord = [center_x + radius * math.cos(tht) for \
         tht in np.linspace(0, 2 * math.pi, res)]
    ycord = [center_y + radius * math.sin(tht) for \
         tht in np.linspace(0, 2 * math.pi, res)]
    return [xcord, ycord]

def gen_square(center_x=0, center_y=0, edge=2):
    """Returns the vertices of a square in [x,y] coordinates, which is centered
    at the center=[x,y] and with the edge length equal to edge"""
    vertices_x = [center_x + edge/2, center_x - \
                  edge/2, center_x - edge/2, center_x + edge/2]
    vertices_y = [center_y + edge/2, center_y + \
                  edge/2, center_y - edge/2, center_y - edge/2]
    vertices = [vertices_x, vertices_y]
    return vertices

PLAY = True
APPROX_PI_LIST = list()
NUM_DARTS_LIST = list()

while PLAY:
    #Insert the number of darts to be thrown
    NUM_DARTS = int( \
            input('Please insert the number of darts that you want to throw\n'))
    NUM_DARTS_LIST.append(NUM_DARTS)

    CIRC_DARTS = {'x':list(), 'y':list()}
    SQUARE_DARTS = {'x':list(), 'y':list()}

    CIRC_HITS = 0
    SQUARE_HITS = 0

    for dart in range(NUM_DARTS):
        x_dart = random.random() * 2 - 1
        y_dart = random.random() * 2 - 1

        if(x_dart**2 + y_dart**2)**(1/2) > 1:
            SQUARE_HITS += 1
            SQUARE_DARTS['x'].append(x_dart)
            SQUARE_DARTS['y'].append(y_dart)

        elif(x_dart**2 + y_dart**2)**(1/2) <= 1:
            CIRC_HITS += 1
            CIRC_DARTS['x'].append(x_dart)
            CIRC_DARTS['y'].append(y_dart)

        else:
            pass

    APPROX_PI = 4 * CIRC_HITS/NUM_DARTS #THE APPROXIMATED VALUE OF PI
    APPROX_PI_LIST.append(APPROX_PI)

    #Plots the darts thrown in a new figure
    plt.figure(figsize=(10, 10))

    #Plots the square
    plt.fill(gen_square()[0], gen_square()[1], fill=False)

    #Plots the circle
    plt.plot(gen_circle()[0], gen_circle()[1], 'g-')

    #Plots the darts which landed on the darts board
    plt.plot(CIRC_DARTS['x'], CIRC_DARTS['y'], 'go')

    #Plots the darts which landed outside the darts board and inside the square
    plt.plot(SQUARE_DARTS['x'], SQUARE_DARTS['y'], 'ro')

    #Sets a title to the plot
    plt.title('Approximated Pi value: {:6.4f} ==> Darts thrown: {:d}'.format( \
            APPROX_PI, NUM_DARTS), {'fontsize':20})

    #Turning off hte tick labels for the plots
    plt.xticks([])
    plt.yticks([])

    print("\nYour darts Monte Carlo method approximative value of PI is:",
          " {}\n\nThat's {} off from the actual value of PI\n".format(\
            APPROX_PI, abs(math.pi - APPROX_PI)))
    print('\nCircle hit {} times and square hit {} times'.format(\
          CIRC_HITS, SQUARE_HITS))

    QUESTION_STRING = 'Do you want to trow darts again Y/N?. \
    To see all the plots press N\n'
    CONTINUE_PLAY = input(QUESTION_STRING)
    if CONTINUE_PLAY == 'Y':
        PLAY = True
    elif CONTINUE_PLAY == 'N':
        PLAY = False
        print('\nThank you for playing the game,',
              ' have a look at all the plots generated\n')
        print('\nThe previous results are:\n')

        for piVal, dart in zip(APPROX_PI_LIST, NUM_DARTS_LIST):
            print(f'Approximated Pi value: {piVal:4} ',
                  f'==> Darts thrown: {dart:4}')
