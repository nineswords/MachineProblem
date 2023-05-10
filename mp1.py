# -*- coding: utf-8 -*-
"""MP1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/nineswords/MachineProblem/blob/main/MP1.ipynb

#Machine Problem
Import Data 

First, you need to install the pandas library if it is not already installed. In Google Colab, you can install it by running the following command:

To import a CSV (Comma-Separated Values) file in Python, you can use the csv module. Here's an example:

Import the csv module:
"""

pip install pandas

import csv

"""Open the CSV file using the open() function and create a csv.reader object:"""

with open('child-health-indicators-for-philippines-41.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)