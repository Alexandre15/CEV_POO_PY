from funcionarios import *


def main():
    f1 = Horista("Alexandre", 12, 200)
    f1.calc_sal()
    f1.analisar_sal()

    f2 = Mensalista("Alex", 9500)
    f2.calc_sal()
    f2.analisar_sal()

if __name__ == "__main__":
    main()