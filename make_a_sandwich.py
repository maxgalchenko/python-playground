def make_sandwich(
    bread_type: str, filling: str, cheese: str = "none", toasted: bool = False
) -> str:
    """making sandwich with provided ingredients

    Args:
        bread_type (str): type of bread
        filling (str): filling
        cheese (str, optional): cheese. Defaults to "none".
        toasted (bool, optional): indicating if the sandwich is toasted. Defaults to False.

    Returns:
        str: process if making it.
    """
    # return f"Making a {"toasted " if toasted else ""}{bread_type} with {filling} and {cheese}"
    return (
        "Making a "
        + ("toasted " if toasted else "")
        + bread_type
        + " sandwich with "
        + filling
        + ((" and " + cheese + " cheese") if cheese != "none" else "")
        + "."
    )


print(make_sandwich("wheat", "turkey", "cheddar", True))
print(make_sandwich("rye", "ham"))
