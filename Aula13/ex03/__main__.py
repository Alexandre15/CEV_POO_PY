from classes import *


def main():
    p1 = Mae("Adriana")
    p2 = Filho("Guilherme")
    p3 = Filha("Emanuele")

    p1.fazer_pudim()
    p1.fritar_coxinha()
    print("\n")

    p2.fazer_pudim()
    p2.fritar_coxinha()
    print("\n")

    p3.fazer_pudim()
    p3.fritar_coxinha()
    print("\n")
if __name__ == "__main__":
    main()
