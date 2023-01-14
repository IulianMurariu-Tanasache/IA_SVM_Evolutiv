from ajustez import functie_activare
from GATE import GATE

class SVM:
    def __init__(self, date_antrenare, date_test):
        self.date_antrenare = date_antrenare
        self.date_test = date_test
        self.alfa = None
        self.bias = None
        self.GATE = GATE(date_antrenare, 20, 0.02, 100)

    def salvare_model(self, path):
        with open(path, 'w') as file:
            file.write('')
            file.write(','.join([str(a) for a in self.alfa]))
            file.write('\n')
            file.write(str(self.bias))

    def incarcare_model(self, path):
        with open(path, 'r') as file:
            lines  = file.readlines()
            self.alfa = [float(a) for a in lines[0].replace('\n','').split(',')]
            self.bias = float(lines[1].replace('\n',''))

    def antrenare(self):
        self.alfa, self.bias = self.GATE.run_algorithm()

    def prezicere(self, z):
        return functie_activare(z, self.date_antrenare, self.alfa, self.bias)