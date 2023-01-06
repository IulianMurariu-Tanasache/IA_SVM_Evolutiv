from scipy.io import arff
import pandas

# data[0] -> datele care nu iss string
# -> data[0] --> array cu data >data[1]  -->artibutele
# df -> tabel cuu date si valori
# data_to_parse --> toate datele sunt unite intr-un string


def incarcare_datele_pentru_antrenare():#incarc datele din fisirerul cu extensia arff
    data = arff.loadarff(r"E:\anul4\IA\Proiectt\IA_SVM_Evolutiv\Training-Dataset-1.arff")
    df = pandas.DataFrame(data[0])
    return data, df