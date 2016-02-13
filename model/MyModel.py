import csv, sys

__author__ = 'Andreas Ernhofer'

class MyModel(object):

    def __init__(self):
        self.filename = '../data/file.csv'

    def loadCSV(self):
        text = ""
        with open(self.filename, newline='') as f:
            reader = csv.reader(f)
            try:
                for row in reader:
                    text += row[0] + "\n"
            except csv.Error as e:
                sys.exit('file {}, line {}: {}'.format(self.filename, reader.line_num, e))
        return text

    def saveCSV(self,text):

        with open(self.filename, 'w', newline='') as fp:
            writer = csv.writer(fp, delimiter=';')
            werte=[]
            zeilen=text.split("\n")
            for zeile in zeilen:
                wertezeile=zeile.split(";")
                werte.append(wertezeile)
            writer.writerows(werte)