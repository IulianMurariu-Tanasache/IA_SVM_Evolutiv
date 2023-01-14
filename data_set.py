import re
import json

#functie ce  returneaza o tupla ce contine o lista de tuple, ficare tupla continand o lista cu elemente si un rezultat
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
            list3[i] = int(list3[i + 1])
        if count < 31:
            new_list.append(int(list3[i][0]))
            count += 1
        elif count == 31:
            # print(new_list)
            #vector_date.append(new_list)
            vector_date.append((new_list[:len(new_list) - 1], new_list[len(new_list) - 1]))
            new_list = []
            count = 0
    #print(vector_date)
    return vector_date


def scriere_fisier(data, fisier):
    with open(f'{fisier}', 'w') as f:
        for i in data:
            f.write(f"{i[0]} ---> {i[1]} ")
            f.write("\n")


def creare_dictionare(vector_date, data): #functie ce coreleaza datele cu semnificatia ficareia
    iesire = {}#ok
    dict = {}
    dict2 = {}
    for i in vector_date:
        count = 0
        for atribut in data:
            # print(f"{atribut} = {site[caracteristici]}")
            if atribut == "Result":
                if i[1] == "-1":
                    dict2["REZULTAT"] = "Suspicios"
                elif i[1] == "0":
                    dict2["REZULTAT"] = "Nesigur"
                elif i[1] == "1":
                    dict2["REZULTAT"] = "Sigur"
            else:
                dict[f"{atribut}"] = i[0][count]
                count += 1
        iesire[json.dumps(dict)] = dict2
    return iesire


def scriere_dictionare_in_fisier(this_list, file_name):
    with open(f'{file_name}', 'w') as f:
        for i in this_list:
            f.write(f"{i} ")
            f.write("\n")