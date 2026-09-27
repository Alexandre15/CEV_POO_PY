from classes import *


def main():
    c1 = Carteira(100)
    c2 = Carteira(100)

    c1 += 50
    c1 -= 10

    if c1 == c2:
        print("Vocês tem o mesmo valor na carteira.")
    else:
        print(f"As carteiras tem valores diferentes: C1 R${c1.saldo} e C2 R${c2.saldo}.")

    print(c1)

if __name__ == "__main__":
    main()
