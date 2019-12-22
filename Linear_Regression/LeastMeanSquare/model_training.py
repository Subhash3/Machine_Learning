#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import csv
import sys
import pickle
from model_class import Model

def check_usage() :
    arguments = sys.argv
    if len(arguments) != 3 :
        print("Usage: ", arguments[0], " <csv-data-set> <File to store Model Object>")
        quit()
    data_file = arguments[1]
    file_extension = data_file.split('.')[-1]
    if file_extension != "csv" :
        print("Data set must be a CSV file")
        quit()
    object_file = arguments[2] + '.pkl'
    return data_file, object_file


def main () :
    dataset_file, object_file = check_usage()

    model = Model()
    model.train(dataset_file)
    model.calc_RSquare()
    model.save_model(object_file)

    while True :
        x = input("Enter an integer: ")
        try :
            x = int(x)
        except :
            quit()
        model.predict(x)

# Start the program from main function
if __name__ == '__main__' :
    main()