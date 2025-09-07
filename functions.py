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


def happy_birthday(age, name):
    """Return happy birthday's congratulation based on the age and name.

    Args:
        age (int): how old is person
        name (str): the person's name
    """
    print(f"Happy Birthday {name} and congratulations on turning  {age} years old!")


print(happy_birthday(22, "Nora"))
