import csv

__author__ = 'Andreas Ernhofer'

class MyModel(object):

    def loadCSV(self):
        text = ""
        with open('../data/file.csv', newline='') as f:
            reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
            for row in reader:
                text += row[0] + "\n"
        return text