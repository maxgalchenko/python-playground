def calculate_diameter_circle(radius: float) -> float:
    """Function that calculates the diameter or circle

    Args:
      radius (float): The radius of the circle.

    Returns:
      float: Diameter of the circle. Will return -1 if radius is negative.

    Raises:

    Example:
      >>> calculate_diameter_circle (3.2)
      6.4
    """
    if radius < 0:
        return -1
    return radius * 2

print(calculate_diameter_circle(7))
print(calculate_diameter_circle(2.5))
print(calculate_diameter_circle(0))
print(calculate_diameter_circle(-3))
print(calculate_diameter_circle(1000000))