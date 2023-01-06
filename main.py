from ajustare.ajustez import functie_activare
from incarcare_date.incarc import incarcare_datele_pentru_antrenare
from parsare.data_set import parsare, incrucisare, scriere_fisier, scriere_fisier_incrucisat

rad = [-1, -1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 1, -1, -1, 0, -1, 1, 1, 0, 1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1]
###-1,1,1,1,-1,-1,-1,-1,-1,1,1,-1,1,-1,1,-1,-1,-1,0,1,1,1,1,-1,-1,-1,-1,1,1,-1
alpha = [-1, -1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 1, -1, -1, 0, -1, 1, 1, 0, 1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1]
data, df = incarcare_datele_pentru_antrenare()  # data contine datele din arff, ce trebuie parsate


def pregatire_date(date):  # imparte setul de date intre cele de antrenare si cele de testare
    date_antrenare = []
    date_testare = []
    for i in range(0, len(date)):
        if i <= (len(date) * 70) / 100:
            date_antrenare.append(date[i])
        else:
            date_testare.append(date[i])
    return date_antrenare, date_testare


date = parsare(data)
antrenare, test = pregatire_date(date)
scriere_fisier(date, "tuple")
this_list = incrucisare(date, df)
scriere_fisier_incrucisat(this_list, "incrucisare")
print(functie_activare(rad, date, date[0], 0.1))

