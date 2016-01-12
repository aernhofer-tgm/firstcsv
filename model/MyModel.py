import csv

__author__ = 'Andreas Ernhofer'

class MyModel(object):

    def loadCSV(self):
        list
        with open('../data/file.csv', newline='') as f:
            reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
            for row in reader:
                print(row)