def is_point_on_line(point, a, b):
    """Sprawdza, czy punkt leży na prostej y = ax + b."""
    return point[1] == a * point[0] + b

def find_parallel_line(a, b, point):
    """Znajduje równanie prostej równoległej przechodzącej przez dany punkt."""
    intercept = point[1] - a * point[0]
    return (a, intercept)

def find_perpendicular_line(a, b, point):
    """Znajduje równanie prostej prostopadłej przechodzącej przez dany punkt."""
    if a == 0:
        raise ValueError("Prosta prostopadła do poziomej jest pionowa (brak współczynnika nachylenia).")
    perpendicular_slope = -1 / a
    intercept = point[1] - perpendicular_slope * point[0]
    return (perpendicular_slope, intercept)