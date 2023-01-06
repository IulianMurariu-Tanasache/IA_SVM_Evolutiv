from ajustez import functie_activare

class SVM:
    def __init__(self, date_antrenare, date_test):
        self.date_antrenare = date_antrenare
        self.date_test = date_test
        self.alfa = None
        self.bias = None

    def antrenare(self):
        #GATE
        pass

    def prezicere(self, z):
        return functie_activare(z, self.antrenare, self.alfa, self.bias)