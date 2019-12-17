#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import csv
import sys
import pickle

class Model() :
    x_column = list()
    y_column = list()
    mean_x = 0
    mean_y = 0
    len_x = 0
    len_y = 0
    m = c = 0
    data_len = 0

    def __parse_dataset(self, dataset_file) :
        # Read the csv dataset
        dataset_filehandler = open(dataset_file)
        csv_data = csv.reader(dataset_filehandler, delimiter=",")

        # Parse data
        for row in csv_data :
            x = float(row[0])
            y = float(row[1])
            self.x_column.append(x)
            self.y_column.append(y)
            self.mean_x += x
            self.mean_y += y
            self.len_x += 1
            self.len_y += 1
        self.mean_x /= self.len_x
        self.mean_y /= self.len_y
        self.data_len = self.len_x

        # return x_column, y_column, mean_x, mean_y, len_x
        return

    def __calc_slope(self, x_values, y_values, mean_x, mean_y, data_len) :
        # calculate m
        numerator = 0 # sum((x-mean_x)(y-mean_y))
        denominator = 0 # sum((x-mean_x)^2)

        # print(numerator, denominator, self.x_column, self.y_column, self.mean_x, self.mean_y)

        for i in range(data_len) :
            numerator += (x_values[i] - mean_x) * (y_values[i] - mean_y)
            denominator += (x_values[i] - mean_x)**2
            # print(numerator, denominator)
        m = numerator/denominator

        return m

    def __calc_intercept(self, x_coord, y_coord, slope) :
        # calculate c
        # c = y_mean - m*x_mean

        c = y_coord - slope * x_coord
        return c

    def train(self, dataset_file) :
        # print("Parsing..")
        self.__parse_dataset(dataset_file)
        # print("Calculating slope")
        self.m = self.__calc_slope(self.x_column, self.y_column, self.mean_x, self.mean_y, self.data_len)
        # print("Calculating Intercept")
        self.c = self.__calc_intercept(self.mean_x, self.mean_y, self.m)

        print("Model trained successfully")

        # return m, c
        return

    def predict(self, x) :
        m = self.m
        c = self.c

        val = m*x + c
        print("f(", x, "): ", val, sep="")
        return val

    def __predictions(self, x_values) :
        y_predicted = list()
        m = self.m
        c = self.c

        for x in x_values :
            val = m*x + c
            y_predicted.append(val)

        return y_predicted

    def calc_RSquare(self) :
        numerator = 0 # sum((yp - y_mean)^2)
        denominator = 0 # sum((y - y_mean)^2)

        original_y = self.y_column
        predicted_y = self.__predictions(self.x_column)
        data_len = self.data_len
        y_mean = self.mean_y

        for i in range(data_len) :
            numerator += (predicted_y[i] - y_mean)**2
            denominator += (original_y[i] - y_mean)**2
        Rs =  numerator/denominator

        print("R^2: ", Rs)
        return Rs
    
def save_model(model, object_file) :
    fp = open(object_file, 'wb')
    pickle.dump(model, fp)
    fp.close()

    return

def check_usage() :
    arguments = sys.argv
    if len(arguments) < 2 :
        print("Usage: ", arguments[0], " <csv-data-set> [File to store Model Object]")
        quit()
    data_file = object_file = None
    if len(arguments) >= 2 :
        data_file = arguments[1]
        file_extension = data_file.split('.')[-1]
        if file_extension != "csv" :
            print("Data set must be a CSV file")
            quit()
    if len(arguments) >= 3 :
        object_file = arguments[2] + '.pkl'
    return data_file, object_file


def main () :
    dataset_file, object_file = check_usage()

    model = Model()
    model.train(dataset_file)
    model.calc_RSquare()
    if object_file != None :
        save_model(model, object_file)

    trained_model = object_file
    fp = open(trained_model ,'rb')
    m = pickle.load(fp)
    print("Loading done")
    while True :
        x = input("Enter an integer: ")
        try :
            x = int(x)
        except :
            quit()
        model.predict(x)
        m.predict(x)

# Start the program from main function
if __name__ == '__main__' :
    main()