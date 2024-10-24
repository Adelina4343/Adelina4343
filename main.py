import numpy as np
import matplotlib.pyplot as plt


# Functie pentru determinarea tipului conicei
def determina_tipul_conicei(A, B, C):
    D = B ** 2 - A * C  # Discriminant
    if D > 0:
        return "Hiperbolă", D
    elif D == 0:
        return "Parabolă", D
    else:
        return "Elipsă", D


# Functie pentru determinarea formei canonice si a asimptotelor
def forma_canonica(A, B, C, E, F, G):
    # Calculeaza centrul
    delta = A * C - B ** 2
    if delta != 0:
        x0 = (C * E - B * F) / delta
        y0 = (A * F - B * E) / delta
    else:
        x0 = y0 = None

    # Determina tipul conicei
    tip, discriminant = determina_tipul_conicei(A, B, C)

    # Calcul asimptote daca este hiperbola
    asimptote = None
    if tip == "Hiperbolă":
        if B == 0:
            asimptote = [f"y = +/- sqrt({-A}/{C}) * x" if C != 0 else "x = +/- sqrt({-C}/{A}) * y"]
        else:
            asimptote = [f"Asimptotele sunt greu de determinat pentru B ≠ 0 fără rotație"]

    return tip, (x0, y0), asimptote


# Functie pentru reprezentarea grafica a conicei
def deseneaza_conica(A, B, C, E, F, G):
    tip, centru, asimptote = forma_canonica(A, B, C, E, F, G)

    # Interval pentru grafic
    x = np.linspace(-10, 10, 400)
    y = np.linspace(-10, 10, 400)
    X, Y = np.meshgrid(x, y)

    # Ecuația conicei
    Z = A * X ** 2 + 2 * B * X * Y + C * Y ** 2 + E * X + F * Y + G

    plt.figure(figsize=(8, 8))
    plt.contour(X, Y, Z, levels=[0], colors='r')
    plt.title(f"Reprezentarea grafică a unei {tip}")

    if centru[0] is not None:
        plt.scatter(centru[0], centru[1], color='blue', label="Centru")

    if asimptote is not None:
        for asimptota in asimptote:
            plt.annotate(asimptota, (0, 0), textcoords="offset points", xytext=(10, -10), ha='center', color='green')

    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()


# Exemplu de utilizare
A, B, C = 1, 0, 5  # Coeficientii conicei
E, F, G = 3, 0, 0  # Termenii liniari si termenul liber
deseneaza_conica(A, B, C, E, F, G)
