from scipy.io import arff
import pandas

# data[0] -> datele care nu iss string
# -> data[0] --> array cu data >data[1]  -->artibutele
# df -> tabel cuu date si valori
# data_to_parse --> toate datele sunt unite intr-un string


def incarcare_datele_pentru_antrenare():#incarc datele din fisirerul cu extensia arff
    data = arff.loadarff(r".\scurt.arff")
    df = pandas.DataFrame(data[0])
    return data, df