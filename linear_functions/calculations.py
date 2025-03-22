def calculate_slope(point1, point2):
    """Oblicza współczynnik nachylenia prostej przechodzącej przez dwa punkty."""
    try:
        return (point2[1] - point1[1]) / (point2[0] - point1[0])
    except ZeroDivisionError:
        raise ValueError("Punkty mają tę samą współrzędną x — prosta pionowa.")

def calculate_intercept(point, slope):
    """Oblicza wyraz wolny funkcji liniowej."""
    return point[1] - slope * point[0]

def solve_linear_equation(a, b, c):
    """Rozwiązuje równanie liniowe ax + b = c."""
    if a == 0:
        raise ValueError("Współczynnik 'a' nie może być zerem.")
    return (c - b) / a
