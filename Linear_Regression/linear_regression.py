#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import csv
import sys

def check_usage() :
    arguments = sys.argv
    if len(arguments) != 2 :
        print("Usage: ", arguments[0], " <csv-data-set>")
        quit()
    data_file = arguments[1]
    file_extension = data_file.split('.')[-1]
    if file_extension != "csv" :
        print("Data set must be a CSV file")
        quit()
    return data_file

def parse_dataset(dataset_file) :
    # Read the csv dataset
    dataset_filehandler = open(dataset_file)
    csv_data = csv.reader(dataset_filehandler, delimiter=",")

    x_column = list()
    y_column = list()
    mean_x = 0
    mean_y = 0
    len_x = 0
    len_y = 0

    # Parse data
    for row in csv_data :
        x = float(row[0])
        y = float(row[1])
        x_column.append(x)
        y_column.append(y)
        mean_x += x
        mean_y += y
        len_x += 1
        len_y += 1
    mean_x /= len_x
    mean_y /= len_y

    return x_column, y_column, mean_x, mean_y, len_x

def calc_slope(data_len, x_values, y_values, mean_x, mean_y) :
    # calculate m
    numerator = 0 # sum((x-mean_x)(y-mean_y))
    denominator = 0 # sum((x-mean_x)^2)

    for i in range(data_len) :
        numerator += (x_values[i] - mean_x) * (y_values[i] - mean_y)
        denominator += (x_values[i] - mean_x)**2
    m = numerator/denominator

    return m

def calc_intercept(x_coord, y_coord, slope) :
    # calculate c
    # c = y_mean - m*x_mean

    c = y_coord - slope * x_coord
    return c

def line_output(x_values, slope, intercept) :
    y_predicted = list()
    m = slope
    c = intercept

    for x in x_values :
        val = m*x + c
        y_predicted.append(val)

    return y_predicted

def calc_RSquare(original_y, predicted_y, y_mean, data_len) :
    numerator = 0 # sum((yp - y_mean)^2)
    denominator = 0 # sum((y - y_mean)^2)

    for i in range(data_len) :
        numerator += (predicted_y[i] - y_mean)**2
        denominator += (original_y[i] - y_mean)**2
    return numerator/denominator

def predict_new(x, m, c) :
    return m*x + c

def main () :
    dataset_file = check_usage()

    # Parse the dataset
    x_column, y_column, mean_x, mean_y, data_len = parse_dataset(dataset_file)

    # Plot the data points
    plt.scatter(x_column, y_column, c="orange", edgecolors="black", label="Data Points")

    # Calculate m and c
    m = calc_slope(data_len, x_column, y_column, mean_x, mean_y)
    print("Slope m: ", m)
    # y = mx + c, through (x_mean, y_mean)
    c = calc_intercept(mean_x, mean_y, m)
    print("Intercept c: ", c)

    # Plot the regression line
    line_x = np.linspace(0, 80, 300) # 300 evenly spaced points over the interval [0, 80]
    line_y = m*line_x + c

    # Get the predicted y values using the regression line
    y_predicted = line_output(x_column, m, c)

    # Calculate R^2
    RSquare = calc_RSquare(y_column, y_predicted, mean_y, data_len)
    print("R^2: ", RSquare)

    # Plot the whole 
    plt.plot(line_x, line_y, label="Line of Regression")

    plt.title("Linear Regression")
    plt.xlabel("X values")
    plt.ylabel("Y values")
    info = ""
    info += "Slope m: " + str(m) + "\n"
    info += "Intercept c: " + str(c) + "\n"
    info += "R^2: " + str(RSquare)[:9]
    plt.text(3, 90, info)
    plt.legend()
    plt.show()

    while True :
        choice = input("Do you want to predict any (Y/n):")
        if choice in ['y', 'Y'] :
            x = int(input("Enter x value: "))
            y = predict_new(x, m, c)
            print("Predicted y:", y)
        else :
            print("Abort")
            quit()


# Start the program from main function
if __name__ == '__main__' :
    main()