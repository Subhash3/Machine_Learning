## Linear Regression  

- ***linear\_regression.py***  
- Accepts a (data set) csv file containing two columns.
- Line of best fit is calculated using **Mean Square Error ** method.
- Given data set and line of best fit are plotted on a 2d graph.  

- ***graphical.py***  
- p5 python3 library is used.
- User is allowed to plot random points on a 500x500 2d plane.
- For each new points plotted by user, a line of best fit is calculated and is drawn on the same plane.
- This file also accepts an optional file name to export data points in csv format.  

- ***model\_training.py***
- A Model class is defined.  
- Accepts a csv file as data set and an optinal a file name to store the serialized Model.  
- A trained model can easily be stored in to a file.  

- ***load\_trained_model.py***
- Accepts a serialized object of a trained model.
