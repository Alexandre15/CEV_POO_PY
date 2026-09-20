from classes import *
from rich import print


def main():
    p1 = Quadrado(20)

    print(f"Perímetro = {p1.perimetro():.1f}")
    print(f"Area = {p1.area():.1f}")

    p2 = Circulo(12)
    
    print(f"Perímetro = {p2.perimetro():.1f}")
    print(f"Area = {p2.area():.1f}")

if __name__ == "__main__":
    main()