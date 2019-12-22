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
    try :
        fp = open(trained_model ,'rb')
    except Exception as e :
        print("Exception occurred while opening file ", trained_model)
        print(e)
    try :
        model = pickle.load(fp)
    except Exception as e :
        print("Exception occurred Loading model ", trained_model)
        print(e)

    # model.calc_RSquare()
    print("-=-= Lets Predict :D =-=-")
    print("Enter any character to quit.")
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