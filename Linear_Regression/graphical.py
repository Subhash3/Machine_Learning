#!/usr/bin/python3

from p5 import *
import sys
# from time import sleep

x = y = 20
width = height = 500
data_points = list()
mean_x = mean_y = 0
sum_x = sum_y = 0
total_data_points = 0
m = 1
c = 0
EXPORT_DATASET = False

# Images of (x, y) w.r.t y = k
def map_point(x, y, k) :
    return x, 2*k-y

def unmap_point(x, y, k) :
    return map_point(x, y, k)

def calc_slope() :
    # sum((x-mean_x)(y-mean_y)) / sum((x-mean_x)^2)
    numerator = denominator = 0

    for i in range(total_data_points) :
        numerator += (data_points[i][0] - mean_x) * (data_points[i][1] - mean_y)
        denominator += (data_points[i][0] - mean_x) * (data_points[i][0] - mean_x)
    
    return numerator / denominator

def calc_intercept(m, x, y) :
    # c = y_mean - m*x_mean
    return y - m*x

def linear_regression() :
    global m, c
    slope = calc_slope()
    intercept = calc_intercept(slope, mean_x, mean_y)

    m = slope
    c = intercept

    return m, c

def draw_line() :
    global m, c
    m = calc_slope()
    c = calc_intercept(m, mean_x, mean_y)

    stroke("orange")
    # x1, y1 = unmap_point(mean_x, mean_y, height/2)
    sample_x = width # Just to draw a big line
    sample_y = m*sample_x + c

    x1, y1 = unmap_point(sample_x, sample_y, height/2)
    x2, y2 = unmap_point(0, c, height/2)

    line((x1, y1), (x2, y2))
    
    return

def setup() :
    size(width, height) # 2d plane
    no_loop() # Do not loop the draw function

def draw() :
    global total_data_points
    background(39, 39, 39)
    stroke(255)

    # Plot the data points on the 2d plane
    for i in range(total_data_points) :
        radius = 8
        fill(255)
        # Unmap the points to convert them to the p5 plane co-ordinate system.
        x, y = unmap_point(data_points[i][0], data_points[i][1], height/2)
        circle((x, y), radius) # Point

    # If there are 2 or more data points, Calculate the line of best fit
    if total_data_points > 1 :
        linear_regression()
        print("Slope(m): ", m, "Intercept(c): ", c, "Total points: ", total_data_points)
        # print(data_points)
        draw_line()

def mouse_pressed() :
    global height, total_data_points, mean_x, mean_y
    global sum_x, sum_y, EXPORT_DATASET

    # print("Mouse location: (", mouse_x, ", ", mouse_y, ")", sep="")
    # Map the points to the real life co-ordinate system.
    x, y = map_point(mouse_x, mouse_y, height/2)
    # print("Mapped Point: (", x, ", ", y, ")", sep="")

    # Don't store duplicates
    if (x, y) not in data_points :
        # If user wants dataset to be exported
        if EXPORT_DATASET :
            export_dataset((x, y))
        data_points.append((x, y))
        total_data_points += 1

        sum_x += x
        sum_y += y
        
        # Update the mean values for every new data point
        mean_x = sum_x / total_data_points
        mean_y = sum_y / total_data_points

    redraw() # Repeat the draw() function once

def export_dataset(point) :
    global fp

    # Write the data point to the file
    fp.write(str(point[0]) + ", " + str(point[1]) + "\n")

    return

if __name__ == '__main__' :
    arguments = sys.argv
    argc = len(arguments)
    print("Usage: ", arguments[0], " [filename to export data]", sep="")
    if argc == 2 :
        file = arguments[1]
        fp = open(file, 'w')
        EXPORT_DATASET = True # User wants the data set
    elif argc > 2 :
        print("Usage: ", arguments[0], " [filename to export data]", sep="")
        quit()
    run()

"""
    (0, 0)        (0, width)
    (height, 0)   (height, width)

    This is how the 2d plane of p5 looks like.

    But in real life, origin (0, 0) is situated at the bottom left corner.
    To map a point of the p5 plane to the real life and viceversa, we have to find its image with respect to the line y = height/2.

    The image of the point (x, y) w.r.t the line y = k, is (x, 2k -y).
    This is exactly what map and unmap functions do.
"""