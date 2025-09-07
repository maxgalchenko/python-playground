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


def calc_sale_price(amount, member):
    """_summary_

    Args:
        amount (float): price without sale
        member (boolean): if client is member

    Returns:
        float: sale price
    """
    if member:
        # Members receive a 15% discount (0.15)
        amount = amount - (amount * 0.15)
    else:
        # Non-members get a 5% discount (0.05)
        amount = amount - (amount * 0.05)

        amount = round(amount, 2)
    amount = round(amount, 2)
    return amount


# Example price (already provided)
full_price = 150.50


shirt_color = "Pink"


def display_color_works(shirt_color):
    print("First shirt color is:", shirt_color)


def display_color_failure(shirt_color):
    # Try to access 'color' directly (this will cause an error)
    print("Your shirt color is:", shirt_color)


# The shirt_color variable is in scope in this function
display_color_works(shirt_color)

# The shirt_color variable is not in scope in this function
display_color_failure(shirt_color)
