from loading.loader import Loader
from datastructures.set import Set
from algorithms.rang import rang
from algorithms.sort import sort
from util.paginacija_rezultata import prikazi_rezultate
import os


def validate(user_input):
    input_list = user_input.split()
    check = -1  # Provera -1 za pocetak, 0 za rec, 1 za operator
    valid = False
    len1 = len(input_list)
    string_list = []
    if len1 > 0:
        valid = True
        i = 0
        for word in input_list:
            i = i + 1
            if is_operator(word):
                if i == len1:
                    valid = False  # Ako je poslednja rec operator, unos nije validan
                    break
                else:
                    if check == -1:
                        valid = False  # Ako je prva rec unosa operator, unos nije validan
                        break
                    elif check == 0:
                        string_list.append(word)
                        check = 1  # Ako je operatoru prethodila rec, zabelezava se da je unesen operator
                    else:
                        valid = False  # Ako je doslo do unosa dva operatora jednog za drugim, unos nije validan
                        break
            else:
                if check == 1 or check == -1:
                    string_list.append(word)
                    check = 0  # Zabelezava se da je unesena rec
                else:
                    string_list.append('or')
                    string_list.append(word)
                    check = 0  # Zabelezava se da je unesena rec
    if valid:
        return string_list


def is_operator(string):
    if string == 'and' or string == 'or' or string == 'not':
        return True
    else:
        return False


def search(search_string):
    words = validate(search_string)
    result_sets = {}
    ret_words = []
    for word in words:
        if not is_operator(word):
            result_sets[word] = trie.find(word)
            ret_words.append(word)
    result = Set()
    operator = None
    for word in words:
        if is_operator(word):
            operator = word
        else:
            if len(result_sets[word]) > 0:
                if operator == 'and':
                    result = result.__and__(result_sets[word])
                elif operator == 'not':
                    result = result.__not__(result_sets[word])
                elif operator == 'or':
                    result = result.__or__(result_sets[word])
                elif operator is None:
                    result = result_sets[word]
    return result, ret_words


if __name__ == '__main__':
    while True:
        path = os.path.abspath(input("Unesite putanju pocetnog direktorijuma za pretragu: "))
        if os.path.exists(path) and os.path.isdir(path):
            loader = Loader(path)
            print("Tekuci direktorijum: \n{}".format(path))
            graph, trie = loader.load_data()
            loader.close_parser()
            break
        else:
            print("Uneli ste neispravnu putanju!")
    while True:
        print("\t1 - Prikazi tekuci direktorijum")
        print("\t2 - Unesite rec za pretragu")
        print("\t3 - Prikazi graph")
        print("\t0 - Kraj programa")

        try:
            usr_input = int(input(">> "))
        except ValueError:
            print("Greska pri unosu!\n")
            continue
        except KeyboardInterrupt:
            break
        if usr_input == 1:
            print("--" * 70)
            print("Tekuci direktorijum: \n{}".format(path))
            print("--" * 70)
        elif usr_input == 2:
            unos = input(">> ")
            results, words_rang = search(unos.lower())
            if len(results) > 0:
                rang_result = rang(graph, trie, results, words_rang)
                list_rang_result = list(rang_result.items())
                sort(list_rang_result, 0, len(list_rang_result) - 1)
                while True:
                    try:
                        unos_dn = input("Da li zelite da prikazete rezultate? [D/N]: ")
                    except KeyboardInterrupt:
                        exit(0)

                    if unos_dn == "D" or unos_dn == "d":
                        print("Ukupan broj straniza iz pretrage [{}]".format(len(results)))
                        try:
                            N = int(input("Unesite broj HTML linkova po stranici prikaza (izlaz - bilo sta osim broja): "))
                        except ValueError:
                            print("Pogresan unos")
                            break

                        prikazi_rezultate(list_rang_result, N)
                        break
                    elif unos_dn == "N" or unos_dn == "n":
                        break
                    else:
                        print("Pogresan unos!")
            else:
                print("--" * 70)
                print("Pretraga je neuspesna!")
                print("--" * 70)
        elif usr_input == 3:
            print("--" * 70)
            print(graph)
            print("--" * 70)
        elif usr_input == 0:
            print("Kraj...")
            exit(0)
