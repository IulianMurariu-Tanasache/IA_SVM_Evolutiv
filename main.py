from ajustez import functie_activare
from incarc import incarcare_datele_pentru_antrenare
from data_set import parsare, creare_dictionare, scriere_fisier, scriere_dictionare_in_fisier
from SVM import SVM
from evaluate import evaluate

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
this_list = creare_dictionare(date, df)

svm = SVM(antrenare, test)
#svm.antrenare()
#svm.salvare_model('./model3')
svm.incarcare_model('./model2')
print(test)
#print(svm.prezicere(test[0][0]), test[0][1])
evaluate(svm, test)


#model1 -> 10 epochs, 100 pop_size, 1000 dataset
#model2 -> 20 epochs, 100 pop_size, 1000 dataset -> nu s-a imbunatatit