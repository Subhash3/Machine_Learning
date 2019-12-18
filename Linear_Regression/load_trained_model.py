#!/usr/bin/python3

import pickle
import sys
from model_class import Model

def check_usage() :
    arguments = sys.argv
    if len(arguments) != 2 :
        print("Usage: ", arguments[0], " <Trained Model (Pickle file)>")
        quit()
    trained_model = arguments[1]

    return trained_model

def main() :
    trained_model = check_usage()
    fp = open(trained_model ,'rb')
    model = pickle.load(fp)

    # model.calc_RSquare()
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