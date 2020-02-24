from loading.loader import Loader


def validate(user_input):
    input_list = user_input.split()
    check = -1  # Provera -1 za pocetak, 0 za rec, 1 za operator
    valid = False
    len1 = len(input_list)
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
                        check = 1  # Ako je operatoru prethodila rec, zabelezava se da je unesen operator
                    else:
                        valid = False  # Ako je doslo do unosa dva operatora jednog za drugim, unos nije validan
                        break
            else:
                if check == 1:
                    check = 0 # Zabelezava se da je unesena rec
                else:
                    check = 0  # Zabelezava se da je unesena rec
    return valid


def is_operator(string):
    if string == 'and' or string == 'or' or string == 'not':
        return True
    else:
        return False


if __name__ == '__main__':
    loader = Loader('python-2.7.7-docs-html')
    graph, trie = loader.load_data()
    print(validate('python or class'))
    print(validate('python class inherit'))
    print(validate('python or class or recursion and flags'))
    print(validate('python or or class'))
    print(validate('python or and class'))
    print(validate('python class and recursion'))
    print(validate('python or class or'))
    print(validate('or python or class'))