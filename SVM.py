from ajustez import functie_activare
from GATE import GATE

class SVM:
    def __init__(self, date_antrenare, date_test):
        self.date_antrenare = date_antrenare
        self.date_test = date_test
        self.alfa = None
        self.bias = None
        self.GATE = GATE(date_antrenare, 3, 0.02)

    def antrenare(self):
        self.alfa, self.bias = self.GATE.run_algorithm()

    def prezicere(self, z):
        return functie_activare(z, self.date_antrenare, self.alfa, self.bias)