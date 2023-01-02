from scipy.io import arff
import pandas
import re
import json

data = arff.loadarff(r"E:\anul4\IA\Proiectt\IA_SVM_Evolutiv\Training-Dataset-1.arff")
df = pandas.DataFrame(data[0])
data_to_parse = str(data[0])


# data[0] -> datele care nu iss string
# -> data[0] --> array cu data >data[1]  -->artibutele
# df -> tabel cuu date si valori
# data_to_parse --> toate datele sunt unite intr-un string

def parsare(data):
    list = []
    list2 = []
    list3 = []
    for i in data[0]:
        linie = ""
        for j in i:
            linie = linie + str(j)
            linie.split(")")
        list.append(linie)
    for line in list:
        list2.append(line.split("b'"))
    for lin in list2:
        for i in lin:
            list3.append(re.findall(r'[+-]?\d+', i))
    count = 0
    new_list = []
    vector_date = []
    for i in range(1, len(list3)):
        if list3[i] == ' ':
            list3[i] = list3[i + 1]
        if count < 31:
            new_list.append(list3[i][0])
            count += 1
        elif count == 31:
            # print(new_list)
            vector_date.append(new_list)
            new_list = []
            count = 0
    return vector_date


def afisare(vector_date):
    for i in vector_date:
        string = "["
        for j in i:
            string = string + j + ","
        string = string + "]"
        # print(string)



def incrucisare(vector_date, data):
    iesire = {}
    tupla_finala = ()
    for site in vector_date:
        tupla  = ()
        tupla_intermediara = []
        for i in range(0, len(site)):
            if i == 30:
                tupla = tupla + (site[i],)
            else:
                tupla_intermediara.append(site[i])
        tupla_finala = tupla_finala + tuple((tupla_intermediara,)) + tupla
        dict = {}
        dict2 = {}
        count = 0
        for atribut in data:
            # print(f"{atribut} = {site[caracteristici]}")
            if atribut == "Result":
                if site[-1] == "-1":
                    dict2["REZULTAT"] = "-1"
                elif site[-1] == "0":
                    dict2["REZULTAT"] = "0"
                elif site[-1] == "1":
                    dict2["REZULTAT"] = "1"
            else:
                dict[f"{atribut}"] = site[count]
                count += 1
        iesire[json.dumps(dict)] = dict2
    #return iesire
    return tupla_finala


# print(data[1])
date = parsare(data)
afisare(date)
this_list = incrucisare(date, df)
with open('date_parsate_tuples', 'w') as f:
    for i in range(0,  len(this_list),2):
        f.write(f"{this_list[i]} --> {this_list[i+1]}")
        f.write("\n")

#json
# with open('date_parsate', 'w') as f:
#     for key, value in this_list.items():
#         f.write(f"{key}:{value}")
#         f.write("\n")
#dic


