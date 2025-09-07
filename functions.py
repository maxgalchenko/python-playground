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


import random


def get_lucky_number():
    """return random number

    Returns:
        float: random number
    """
    lucky_num = random.randint(1, 100)
    return lucky_num


lucky_number = get_lucky_number()

print("Your lucky number is:", lucky_number)
