import random


def produsul_scalar(data_calcul, vector):
    rezultat =0
    for i in range(0, len(vector)):
        rezultat += int(data_calcul[i]) * int(vector[i])
    return rezultat


def sign(suma):
    if suma == 0: return 0
    else:
        return 1 if suma > 0 else -1


def functie_activare(date_calcul, vector_intrare, alpha, bias):
    suma = 0
    rez = 0
    produs = 0
    for i in range(0, len(vector_intrare)):
        produs += produsul_scalar(vector_intrare[i][0], date_calcul)
        suma += int(alpha[0][0]) * int(vector_intrare[i][1]) * int(produs)#alfa vector cu 11054 elemente si o sa fie alpfa[i]
    return sign(suma)


def alegere_delta_pozitiv(rezultat):
    return 1 if rezultat == 1 else 0


def alegere_delta_negativ(rezultat):
    return 1 if rezultat == -1 else 0


def suma_alfa_y(alpha, vector_intrare):
    suma = 0
    for i in range(0, len(alpha)):
        suma = suma + alpha[i] * vector_intrare[i][1]

    return suma


def ajustare(alpha, vector_intrare):
    new_alpha = [x for x in alpha]
    suma = suma_alfa_y(alpha, vector_intrare)

    while suma != 0:
        s_pozitiv = 0
        s_negativ = 0
        for j in range(0, len(new_alpha)):
            delta_pozitiv = alegere_delta_pozitiv(vector_intrare[j][1])
            delta_negativ = alegere_delta_negativ(vector_intrare[j][1])
            s_pozitiv += new_alpha[j] * vector_intrare[j][1] * delta_pozitiv
            s_negativ += new_alpha[j] * vector_intrare[j][1] * delta_negativ

        k = random.randint(0, len(vector_intrare))
        if s_pozitiv > s_negativ:
            while vector_intrare[k][1] != 1:
                if vector_intrare[k][1] == 1:
                    break
                else:
                    k = random.randint(0, len(vector_intrare))  # de verificat daca vector_intrare[k][1] = 1
        else:
            while vector_intrare[k][1] != -1:
                if vector_intrare[k][1] == -1:
                    break
                else:
                    k = random.randint(0, len(vector_intrare))  # de verificat daca vector_intrare[k][1] = 1
        if new_alpha[k] > suma:
            new_alpha[k] = new_alpha[k] - suma
        else:
            new_alpha[k] = 0

        suma = suma_alfa_y(new_alpha, vector_intrare)

    return new_alpha