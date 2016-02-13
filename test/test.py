# -*- coding: utf-8 -*-
"""
Hallo
"""

from model.MyModel import MyModel

__author__ = 'andie'

class Test(object):

    def __init__(self):
        """
        
        :return:
        """
        self.model = MyModel()
        self.model.setPath("data/file.csv")

    def test01_save(self):
        """
        Save
        Fungiert wie @Before
        :return:
        """
        self.model.saveCSV("a;b;c;\nd;e\nf")
        assert 1 == 1 #Es ist kein Fehler beim speichern aufgetreten

    def test02_load(self):
        """
        Load
        :return:
        """
        print(self.model.loadCSV())
        assert self.model.loadCSV() == "a;b;c;\nd;e\nf\n"


    def test03_SaveLoad(self):
        """

        :return:
        """
        text = "z;x;\nh;i\nu;e;"
        self.model.saveCSV(text)
        assert self.model.loadCSV() == text+"\n"

    def test04_SaveSave(self):
        """
        Es ist möglich das file oeffter hinter einander zu beschreibem.
        :return:
        """
        text = "z;xjzhguz;\nh;i\nu;e;"
        self.model.saveCSV(text)
        self.model.saveCSV(text)
        assert self.model.loadCSV() == text+"\n"

    def test05_LoadLoad(self):
        """
        Oefter laden
        :return:
        """
        self.model.loadCSV()
        assert self.model.loadCSV() == "z;xjzhguz;\nh;i\nu;e;\n";
