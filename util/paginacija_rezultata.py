def prikazi_rezultate(list, N):
    i = 0
    n = N
    while True:
        print(" -- " * 70)
        print("HTML page" + " " * 100 + "RANG")
        for k in range(i*n, i*n+n):
            if k < len(list):
                line = list[k]
                print(" {}                 {}".format(str(line[0]), str(line[1])))

        print("--" * 70)
        print("\nOpcije:\n\t(+) prikaz sledecih N stranica\n\t(-) prikaz prethodnih N stranica")
        print("\t(n) promena broja stranica koje se prikazuju\n\t(q) izlaz")

        try:
            unos = str(input(">> "))
        except KeyboardInterrupt:
            return 0

        if unos == "q":
            return
        elif unos == "+":
            if i+1 <= int(len(list)/n):
                i += 1
        elif unos == "-":
            if i-1 >= 0:
                i -= 1
        elif unos == "n" :
            n = int(input("Unesite novo N: "))
            i = 0