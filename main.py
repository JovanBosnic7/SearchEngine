from loading.loader import Loader


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
                    check = 0 # Zabelezava se da je unesena rec
                else:
                    string_list.append('or')
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
    for word in words:
        if not is_operator(word):
            result_sets[word] = trie.find(word)


if __name__ == '__main__':
    loader = Loader('python-2.7.7-docs-html')
    graph, trie = loader.load_data()
    search('recursion and access')