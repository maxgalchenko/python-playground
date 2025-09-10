def get_unique_numbers(items: list[int]) -> list[int]:
    """returns only unique numbers in the list

    Args:
        items (list[int]): list of numbers

    Returns:
        list[int]: list of unique numbers
    """
    return list(set(items))

numbers = [1, 2, 2, 3, 1, 4, 5, 3]

print(get_unique_numbers(numbers))