#!/usr/bin/python3

import csv
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

    Learning_rate = 0.1
    iterations = 1000

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

    def compute_error(self) :
        N = self.data_len
        X = self.x_column
        Y = self.y_column
        m = self.m
        c = self.c
        error = 0

        for i in range(N) :
            error += 1/N * (Y[i] - (m*X[i] + c)) ** 2

        return error

    def train(self, dataset_file) : # Using gradient descent
        self.__parse_dataset(dataset_file)
        m = 0
        c = 0
        iterations = self.iterations
        X = self.x_column
        Y = self.y_column
        N = self.data_len
        L = self.Learning_rate

        print("X: ", X, "Y: ", Y, "N: ", N, "L: ", L)

        for i in range(iterations) :
            error = self.compute_error()
            print("Error: ", str(error)[:5], "m: ", m, "c: ", c)
            Dm = 0
            for j in range(N) :
                Dm += (-2/N) * (Y[j] - (m*X[j] + c)) * X[j]

            Dc = 0
            for j in range(N) :
                Dc += (-2/N) * (Y[j] - (m*X[j] + c))

            print("Dm: ", str(Dm)[:5], "Dc: ", str(Dc)[:5])


            m = m - Dm*L
            c = m - Dc*L

            self.m = m
            self.c = c

        print("Model Trained successfully using Gradient Descent")
        return m, c

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
    
    def save_model(self, object_file) :
        fp = open(object_file, 'wb')
        pickle.dump(self, fp)
        fp.close()

        print("Model successfully saved to ", object_file)

        return
