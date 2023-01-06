from ajustare.ajustez import functie_activare
from incarcare_date.incarc import incarcare_datele_pentru_antrenare
from parsare.data_set import parsare, incrucisare, scriere_fisier, scriere_fisier_incrucisat

rad = [-1, -1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 1, -1, -1, 0, -1, 1, 1, 0, 1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1]
###-1,1,1,1,-1,-1,-1,-1,-1,1,1,-1,1,-1,1,-1,-1,-1,0,1,1,1,1,-1,-1,-1,-1,1,1,-1
alpha = [-1, -1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 1, -1, -1, 0, -1, 1, 1, 0, 1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1]

data, df = incarcare_datele_pentru_antrenare()
date = parsare(data)
scriere_fisier(date, "tuple")
this_list = incrucisare(date, df)
scriere_fisier_incrucisat(this_list, "incrucisare")

print(functie_activare(rad, date, date[0],0.1))


#print(functie_activare(rad, this_list, alpha, 0.1))
#scriere_fisier(this_list)
# for i in range(0, len(this_list), 2):
#     print(f"{this_list[i]} --> {this_list[i + 1]}")
