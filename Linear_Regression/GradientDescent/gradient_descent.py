#!/usr/bin/python3

from model_class import Model
import sys

def make_predictions(model) :
    while True :
        x = input()
        try :
            x = int(x)
        except :
            break
        model.predict(x)
    return        

def main() :
    args = sys.argv
    argc = len(args)

    if argc != 2 :
        print("Usage: ", args[0], " <csv data file>")
        quit()
    datafile = args[1]
    model = Model()
    m, c = model.train(datafile)
    print("Slope(m): ", m, "Intercept(c): ", c)

    choice = input("Do you want to make predictions(Y/n): ")
    if choice in ['y', 'Y'] :
        print("Enter any character to stop predictions")
        make_predictions(model)
    else :
        choice = input("Do you want to SAVE the trained model?(Y/n): ")
        if choice in ['y', 'Y'] :
            while True :
                file = input("Please provide a file to save the model: ")
                try :
                    fp = open(file, "wb")
                    fp.close()
                    model.save_model(file)
                    quit()
                except Exception as e :
                    print("Exception occurred while opening the file ", file)
                    print(e)
        else :
            print("Abort")

if __name__ == "__main__":
    main()