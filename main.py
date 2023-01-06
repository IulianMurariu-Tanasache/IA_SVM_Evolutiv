from ajustez import functie_activare
from incarc import incarcare_datele_pentru_antrenare
from data_set import parsare, creare_dictionare, scriere_fisier, scriere_dictionare_in_fisier
from SVM import SVM

rad = [-1, -1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 1, -1, -1, 0, -1, 1, 1, 0, 1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1]
###-1,1,1,1,-1,-1,-1,-1,-1,1,1,-1,1,-1,1,-1,-1,-1,0,1,1,1,1,-1,-1,-1,-1,1,1,-1
data, df = incarcare_datele_pentru_antrenare()  # data contine datele din arff, ce trebuie parsate


def pregatire_date(date):  # imparte setul de date intre cele de antrenare si cele de testare
    date_antrenare = []
    date_testare = []
    for i in range(0, len(date)):
        if i <= int((len(date) * 70) / 100):
            date_antrenare.append(date[i])
        else:
            date_testare.append(date[i])
    return date_antrenare, date_testare


date = parsare(data)
antrenare, test = pregatire_date(date)
#scriere_fisier(date, "tuple")
this_list = creare_dictionare(date, df)
#scriere_dictionare_in_fisier(this_list, "incrucisare")
#print(functie_activare(rad, date, date[0], 0.1))

svm = SVM(antrenare, test)
svm.antrenare()
print(test[0])
print(svm.prezicere(test[0][0]), test[0][1])